# Generated by Django 5.0.1 on 2024-01-08 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_dessertcake_desserticecream_dessertsnake_juicecoffee_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='desserticecream',
            options={'verbose_name': 'Десерт: Мороженое', 'verbose_name_plural': 'Десерты: Мороженое'},
        ),
        migrations.AlterModelOptions(
            name='juicecoffee',
            options={'verbose_name': 'Напитки:  Кофе', 'verbose_name_plural': 'Напитки: Кофе'},
        ),
    ]
