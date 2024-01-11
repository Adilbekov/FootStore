from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Donuts(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='Donuts_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    old_prise = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    prise = models.CharField(
        verbose_name = 'Цена со скидкой',
        max_length = 255
    )
    image1 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image11'
    )
    image2 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image22'
    )
    image3 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image33'
    )
    image4 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image44'
    )
    description1 = models.TextField(
        verbose_name = 'Описание',
        max_length = 255
    )
    description2 = RichTextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return f'{self.name} - {self.prise}'
    
    class Meta:
        verbose_name = 'Пончик(home)'
        verbose_name_plural = 'Пончики(home)'


class Bread(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='Donuts_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    old_prise = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    prise = models.CharField(
        verbose_name = 'Цена со скидкой',
        max_length = 255
    )
    image1 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image12'
    )
    image2 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image23'
    )
    image3 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image34'
    )
    image4 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image4'
    )
    description1 = models.TextField(
        verbose_name = 'Описание',
        max_length = 255
    )
    description2 = RichTextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return f'{self.name} - {self.prise}'
    
    class Meta:
        verbose_name = 'Хлеб(home)'
        verbose_name_plural = 'Хлеб(home)'


class Cake(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='Donuts_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    old_prise = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    prise = models.CharField(
        verbose_name = 'Цена со скидкой',
        max_length = 255
    )
    image1 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image111'
    )
    image2 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image222'
    )
    image3 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image333'
    )
    image4 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image444'
    )
    description1 = models.TextField(
        verbose_name = 'Описание',
        max_length = 255
    )
    description2 = RichTextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return f'{self.name} - {self.prise}'
    
    class Meta:
        verbose_name = 'Торт(home)'
        verbose_name_plural = 'Торты(home)'


class LowPrice(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена со скидкой',
        max_length = 255
    )
    image1 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image1'
    )
    image2 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image2'
    )
    image3 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image3'
    )
    image4 = models.ImageField(
        verbose_name='Фотография',
        upload_to='LowPrice_image4'
    )
    description1 = models.TextField(
        verbose_name = 'Описание',
        max_length = 255
    )
    description2 = RichTextField(
        verbose_name = 'Описание'
    )
    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Продукт с низким ценником(home)'
        verbose_name_plural = 'Продукты с низкими ценами(home)'