# Generated by Django 5.0.1 on 2024-01-09 13:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='descriptions2',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='descriptions3',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image2',
            field=models.ImageField(default=1, upload_to='BlogPost_image2', verbose_name='Фотография'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image3',
            field=models.ImageField(default=41, upload_to='BlogPost_image3', verbose_name='Фотография'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default=1, max_length=255, verbose_name='Заголовок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='zacrep',
            field=models.CharField(default=1, max_length=255, verbose_name='Закрепленные слова'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='descriptions',
            field=ckeditor.fields.RichTextField(verbose_name='Название'),
        ),
    ]
