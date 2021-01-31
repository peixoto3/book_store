from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import BookSerializer, BookReservationSerializer
from .models import Book, BookReservation
from client.models import Client

from rest_framework import viewsets
from rest_framework import status


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['put'])
    def reserve(self, request, pk=None):
        book = self.get_object()
        reserve_payload = {'book': pk, 'client': request.data.get('client', None)}
        book_reservation_serializer = BookReservationSerializer(data=reserve_payload)
        book_reservation_serializer.is_valid(raise_exception=True)
        book_reservation_serializer.save()

        book.reserved = True
        book.save()
        return Response({'data': {'message': 'Livro reservado com sucesso!'}}, status=status.HTTP_200_OK)

    def delivery(self, request, pk=None):
        pass
