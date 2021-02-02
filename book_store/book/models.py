from decimal import Decimal

from django.db import models
import datetime

from client.models import Client
from .util import CalculatorPenalty, CalculatorInterestPerDay


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    numbers_pages = models.IntegerField()
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2)
    reserved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        unique_together = ['title', 'author']

    def __str__(self):
        return f'{self.title}, {self.author}'


class BookReservation(models.Model):
    DAYS_RENTED_WITHOUT_PENALTY = 3

    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='reserved_books')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Reserva de Livro'
        verbose_name_plural = 'Reserva de Livros'

    def __str__(self):
        return f'{self.book}, {self.client.name}, {self.date}'

    def save(self, *args, **kwargs):
        super(BookReservation, self).save(*args, **kwargs)
        book = self.book
        book.reserved = True
        book.save()

    @property
    def days_of_delay(self):
        today = datetime.date.today()

        rented_days = today - self.date
        if rented_days.days <= self.DAYS_RENTED_WITHOUT_PENALTY:
            return 0

        days_of_delay = rented_days.days - self.DAYS_RENTED_WITHOUT_PENALTY
        return days_of_delay

    def calculate_penalty(self):
        if not self.days_of_delay:
            return Decimal(0)

        calculate_penalty = CalculatorPenalty(self.days_of_delay)
        return calculate_penalty.calculate(self.book.reserve_price)

    def calculate_interest_per_day(self):
        if not self.days_of_delay:
            return Decimal(0)

        interest_per_day = CalculatorInterestPerDay(self.days_of_delay)
        return interest_per_day.calculate(self.book.reserve_price)
