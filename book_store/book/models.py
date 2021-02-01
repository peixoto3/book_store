from decimal import Decimal

from django.db import models
import datetime

from client.models import Client


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    numbers_pages = models.IntegerField()
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2)
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        unique_together = ['title', 'author']


class BookReservation(models.Model):
    DAYS_RENTED_WITHOUT_PENALTY = 3
    THREE_PERCENT_TAX = 0.03
    FIVE_PERCENT_TAX = 0.05
    SEVEN_PERCENT_TAX = 0.07

    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)

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

    def get_days_of_delay(self):
        today = datetime.date.today()

        rented_days = today - self.date
        if rented_days.days <= self.DAYS_RENTED_WITHOUT_PENALTY:
            return 0

        days_of_delay = rented_days.days - self.DAYS_RENTED_WITHOUT_PENALTY
        return days_of_delay

    def _calculate_penalty(self, tax):
        """Calcula a multa a partir do percentual (tax) sobre o valor da reserva"""
        return self.book.reserve_price * Decimal(tax)

    def value_penalty(self):
        days_of_delay = self.get_days_of_delay()

        if not days_of_delay:
            return 0

        if 0 < days_of_delay <= 3:
            return self._calculate_penalty(self.THREE_PERCENT_TAX)

        if 3 < days_of_delay <= 5:
            return self._calculate_penalty(self.FIVE_PERCENT_TAX)

        if days_of_delay > 5:
            return self._calculate_penalty(self.SEVEN_PERCENT_TAX)
