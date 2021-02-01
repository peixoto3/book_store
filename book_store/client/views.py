from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Client
from book.models import BookReservation
from book.serializers import BookReservationDetailSerializer
from .serializers import ClientSerializer

from rest_framework import viewsets


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        client = self.get_object()
        reserved_books = BookReservation.objects.filter(client=client)
        reserved_books_serializers = BookReservationDetailSerializer(reserved_books, many=True)
        return Response(reserved_books_serializers.data, status=status.HTTP_200_OK)
