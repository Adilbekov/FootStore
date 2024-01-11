# Generated by Django 5.0.1 on 2024-01-06 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='Slide_image', verbose_name='Фотография')),
                ('back_image', models.ImageField(upload_to='Slide_back_image', verbose_name='Фотография заднего фона')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('profession', models.CharField(max_length=255, verbose_name='Должность')),
                ('photo', models.ImageField(upload_to='Slide_photo', verbose_name='Фотография данной личности')),
            ],
        ),
    ]