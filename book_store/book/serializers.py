from decimal import Decimal

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
    class Meta:
        model = BookReservation
        fields = ['price', 'book', 'client']


class BookReservationDetailSerializer(serializers.ModelSerializer):
    book_name = serializers.SerializerMethodField()
    penalty = serializers.SerializerMethodField()
    interest_per_day = serializers.SerializerMethodField()
    days_of_delay = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    def get_penalty(self, obj):
        return obj.value_penalty()

    def get_interest_per_day(self, obj):
        return 0.00

    def validate_book(self, book):
        if book.reserved:
            raise serializers.ValidationError("O livro já está reservado")
        return book

    def get_book_name(self, obj):
        return obj.book.title

    def get_days_of_delay(self, obj):
        return obj.get_days_of_delay()

    def get_total_price(self, obj):
        return obj.price + obj.value_penalty()

    class Meta:
        model = BookReservation
        fields = [
            'date',
            'delivery_date',
            'book_name',
            'price',
            'days_of_delay',
            'penalty',
            'interest_per_day',
            'total_price'
        ]
