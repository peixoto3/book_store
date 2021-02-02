# Generated by Django 3.1.5 on 2021-02-01 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20210130_2019'),
        ('book', '0006_auto_20210201_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreservation',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.book'),
        ),
        migrations.AlterField(
            model_name='bookreservation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reserved_books', to='client.client'),
        ),
    ]
