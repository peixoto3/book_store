# Generated by Django 3.1.5 on 2021-02-01 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20210131_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='reserve_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
