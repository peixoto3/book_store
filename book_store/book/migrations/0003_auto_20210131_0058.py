# Generated by Django 3.1.5 on 2021-01-31 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_bookreservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreservation',
            name='delivery_date',
            field=models.DateField(null=True),
        ),
    ]
