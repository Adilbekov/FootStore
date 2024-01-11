# Generated by Django 5.0.1 on 2024-01-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_backimage_image5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donuts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Donuts_image', verbose_name='Фотография')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('old_prise', models.CharField(max_length=255, verbose_name='Прошлая цена')),
                ('prise', models.CharField(max_length=255, verbose_name='Цена со скидкой')),
            ],
        ),
    ]
