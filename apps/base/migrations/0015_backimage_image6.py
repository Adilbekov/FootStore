# Generated by Django 5.0.1 on 2024-01-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_ass_assphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='backimage',
            name='image6',
            field=models.ImageField(default=1, upload_to='BackImage_image6', verbose_name='Фотография для заднего фона'),
            preserve_default=False,
        ),
    ]
