# Generated by Django 5.0.1 on 2024-01-08 09:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0004_advertising'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='BlogPost_image', verbose_name='Фотография')),
                ('descriptions', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('profeshion', models.CharField(max_length=255, verbose_name='Профессия')),
                ('about', models.CharField(max_length=255, verbose_name='О чем идет новость')),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
