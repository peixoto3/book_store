from .models import Book, BookReservation

from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return 'Emprestado' if obj.reserved else 'Disponível'

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'numbers_pages', 'status']


class BookReservationSerializer(serializers.ModelSerializer):
    def validate_book(self, book):
        if book.reserved:
            raise serializers.ValidationError("O livro já está reservado")
        return book

    class Meta:
        model = BookReservation
        fields = '__all__'
