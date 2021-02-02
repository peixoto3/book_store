from client.models import Client
from client.serializers import ClientSerializer

from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

from book.models import Book, BookReservation

from book.serializers import BookReservationDetailSerializer


class ClientTests(APITestCase):

    def setUp(self):
        self.rodrigo = Client.objects.create(name='Rodrigo Peixoto')
        self.carol = Client.objects.create(name='Carolina Peixoto')
        self.teo = Client.objects.create(name='Teofanes Souza')

    def test_get_all_clients(self):
        url = reverse('client-list')
        response = self.client.get(url)
        all_clients = Client.objects.all()
        clients_serializer = ClientSerializer(all_clients, many=True)
        self.assertEqual(response.data, clients_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_client(self):
        url = reverse('client-detail', kwargs={'pk': self.rodrigo.pk})
        client_expected = ClientSerializer(self.rodrigo)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, client_expected.data)

    def test_get_single_client_not_found(self):
        url = reverse('client-detail', kwargs={'pk': 50})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_client(self):
        url = reverse('client-list')
        data = {'name': 'Guilherme Peixoto de Souza'}
        response = self.client.post(url, data, format='json')
        client_expected = Client.objects.get(name='Guilherme Peixoto de Souza')
        client_expected_serializer = ClientSerializer(client_expected)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, client_expected_serializer.data)

    def test_create_client_invalid(self):
        url = reverse('client-list')
        invalid_payload = {}
        response = self.client.post(url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'][0], 'Este campo é obrigatório.')

    def test_create_client_already_existent(self):
        url = reverse('client-list')
        invalid_payload = {'name': 'Carolina Peixoto'}
        response = self.client.post(url, invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'][0], 'Cliente com este name já existe.')

    def test_update_client(self):
        url = reverse('client-detail', kwargs={'pk': self.carol.pk})

        client_payload_update = {
            'name': 'Carolina Peixoto Barbosa'
        }

        client_payload_expected = {
            'id': self.carol.pk,
            'name': 'Carolina Peixoto Barbosa'
        }

        response = self.client.put(url, client_payload_update, format='json')
        self.assertEqual(response.data, client_payload_expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_client(self):
        url = reverse('client-detail', kwargs={'pk': self.teo.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_books_reserved_by_client(self):
        book = Book.objects.create(
            title='Livro de Programação',
            author='Autor de programação',
            numbers_pages=200,
            reserve_price=100
        )
        Book.objects.create(
            title='Livro de Programação II',
            author='Autor de programação II',
            numbers_pages=200,
            reserve_price=100
        )
        BookReservation.objects.create(
            book=book,
            client=self.carol
        )
        reserved_books = BookReservationDetailSerializer(self.carol.reserved_books, many=True)
        url = reverse('client-books', kwargs={'pk': self.carol.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, reserved_books.data)
