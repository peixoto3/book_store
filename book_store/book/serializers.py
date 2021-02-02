from .models import Book, BookReservation

from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return 'Emprestado' if obj.reserved else 'Disponível'

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'numbers_pages', 'reserve_price', 'status']


class BookReservationSerializer(serializers.ModelSerializer):
    def validate_book(self, book):
        if book.reserved:
            raise serializers.ValidationError("O livro já está reservado")
        return book

    class Meta:
        model = BookReservation
        fields = ['book', 'client']


class BookReservationDetailSerializer(serializers.ModelSerializer):
    book_name = serializers.SerializerMethodField()
    penalty = serializers.SerializerMethodField()
    interest_per_day = serializers.SerializerMethodField()
    days_of_delay = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    def get_penalty(self, obj):
        return obj.calculate_penalty()

    def get_interest_per_day(self, obj):
        return obj.calculate_interest_per_day()

    def get_book_name(self, obj):
        return obj.book.title

    def get_days_of_delay(self, obj):
        return obj.days_of_delay

    def get_total_price(self, obj):
        return obj.book.reserve_price + obj.calculate_penalty() + obj.calculate_interest_per_day()

    class Meta:
        model = BookReservation
        fields = [
            'date',
            'delivery_date',
            'book_name',
            'days_of_delay',
            'penalty',
            'interest_per_day',
            'total_price'
        ]
