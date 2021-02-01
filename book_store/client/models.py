from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name
