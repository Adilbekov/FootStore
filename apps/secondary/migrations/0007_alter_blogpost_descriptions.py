# Generated by Django 5.0.1 on 2024-01-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0006_blogpost_descriptions2_blogpost_descriptions3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='descriptions',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
