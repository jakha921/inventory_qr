# Generated by Django 4.2.5 on 2023-10-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_warehouse_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Narxi'),
        ),
    ]
