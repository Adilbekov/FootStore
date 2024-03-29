# Generated by Django 5.0.1 on 2024-01-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FootBurger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='SetFamily_image', verbose_name='Фотография')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('old_price', models.CharField(max_length=255, verbose_name='Прошлая цена')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Fast-Food: Бургер',
                'verbose_name_plural': 'Fast-Food: Бургеры',
            },
        ),
        migrations.CreateModel(
            name='FootPasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='SetFamily_image', verbose_name='Фотография')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('old_price', models.CharField(max_length=255, verbose_name='Прошлая цена')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Fast-Food: Паста',
                'verbose_name_plural': 'Fast-Food: Пасты',
            },
        ),
        migrations.CreateModel(
            name='FootPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='SetFamily_image', verbose_name='Фотография')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('old_price', models.CharField(max_length=255, verbose_name='Прошлая цена')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Fast-Food: Питца',
                'verbose_name_plural': 'Fast-Food: Питцы',
            },
        ),
        migrations.AlterModelOptions(
            name='setcouple',
            options={'verbose_name': 'Сет для пар', 'verbose_name_plural': 'Сет для пары'},
        ),
    ]
