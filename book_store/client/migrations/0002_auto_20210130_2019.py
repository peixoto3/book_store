# Generated by Django 3.1.5 on 2021-01-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]