from decimal import Decimal

from rest_framework.decorators import action
from rest_framework.response import Response

from client.models import Client
from .models import Book

from rest_framework import viewsets
from rest_framework import status
from .serializers import BookSerializer, BookReservationSerializer

BOOK_RESERVED_SUCCESS_MESSAGE = 'Livro reservado com sucesso!'


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def reserve(self, request, pk=None):
        reserve_payload = {
            'client': request.data.get('client', None),
            'price': request.data.get('price', 0),
            'book': pk
        }
        book_reservation_serializer = BookReservationSerializer(data=reserve_payload)
        book_reservation_serializer.is_valid(raise_exception=True)
        book_reservation_serializer.save()

        return Response({'data': {'message': BOOK_RESERVED_SUCCESS_MESSAGE}}, status=status.HTTP_200_OK)

    def delivery(self, request, pk=None):
        pass
