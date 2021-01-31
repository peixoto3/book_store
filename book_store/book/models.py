from django.db import models

from client.models import Client


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    numbers_pages = models.IntegerField()
    reserved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        unique_together = ['title', 'author']


class BookReservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.book}, {self.client.name}, {self.date}'

    class Meta:
        verbose_name = 'Reserva de Livro'
        verbose_name_plural = 'Reserva de Livros'
