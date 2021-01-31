from book.models import Book
from book.serializers import BookSerializer

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class BookTests(APITestCase):

    def setUp(self):
        self.book_programming = Book.objects.create(
            title='Algoritmos',
            author='Thomas Cormen',
            numbers_pages=13212
        )
        self.book_mathematics = Book.objects.create(
            title='Mathematics',
            author='Autor 01',
            numbers_pages=600
        )
        self.book_clean_code = Book.objects.create(
            title='Clean Code',
            author='Robert C. Martin',
            numbers_pages=456
        )

    def test_get_all_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        books_expected = Book.objects.all()
        books_expected_serializers = BookSerializer(books_expected, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, books_expected_serializers.data)

    def test_get_single_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book_clean_code.pk})
        book_expected = BookSerializer(self.book_clean_code)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, book_expected.data)

    def test_get_single_book_not_found(self):
        url = reverse('book-detail', kwargs={'pk': 55})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'Fluent Python',
            'author': 'Luciano Ramalho',
            'numbers_pages': 800,
        }
        response = self.client.post(url, data, format='json')
        book_expected = Book.objects.get(title='Fluent Python', author='Luciano Ramalho')
        book_expected_serializer = BookSerializer(book_expected)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, book_expected_serializer.data)

    def test_create_book_invalid(self):
        url = reverse('book-list')
        invalid_payload = {}
        message_error_field_expected = 'Este campo é obrigatório.'
        response = self.client.post(url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'][0], message_error_field_expected)
        self.assertEqual(response.data['author'][0], message_error_field_expected)
        self.assertEqual(response.data['numbers_pages'][0], message_error_field_expected)

    def test_create_book_already_existent(self):
        url = reverse('book-list')
        invalid_payload = {
            'title': 'Algoritmos',
            'author': 'Thomas Cormen',
            'numbers_pages': 100
        }
        response = self.client.post(url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], 'Os campos title, author devem criar um set único.')

    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book_clean_code.pk})
        book_payload_update = {
            'title': 'Código Limpo',
            'author': 'Robert C. Martin',
            'numbers_pages': 456
        }
        book_payload_expected = {
            'id': self.book_clean_code.pk,
            'title': 'Código Limpo',
            'author': 'Robert C. Martin',
            'numbers_pages': 456,
            'status': 'Disponível'
        }
        response = self.client.put(url, book_payload_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, book_payload_expected)
