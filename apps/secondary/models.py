from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Slide(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название'
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        verbose_name = 'Фотография',
        upload_to='Slide_image'
    )
    name = models.CharField(
        max_length = 255,
        verbose_name = 'Имя'
    )
    profession = models.CharField(
        max_length = 255,
        verbose_name = 'Должность'
    )
    photo = models.ImageField(
        verbose_name = 'Фотография данной личности',
        upload_to='Slide_photo'
    )

    def __str__(self):
        return f'{self.title} - {self.description}'
    
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

class Quality(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    image = models.ImageField(
        verbose_name= 'Фотография',
        upload_to = 'Quality_image'
    )
    info1 = models.TextField(
        verbose_name = 'Информация'
    )
    info2 = models.TextField(
        verbose_name = 'Информация'
    )
    info3 = models.TextField(
        verbose_name = 'Информация'
    )
    info4 = models.TextField(
        verbose_name = 'Информация'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Качество наших услуг'
        verbose_name_plural = 'Качество наших услуг'

class Foot(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='Foot_image'
    )
    name = models.CharField(
        verbose_name = 'Название продукта',
        max_length = 255
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Выпечка'
        verbose_name_plural = 'Выпечки'


class Advertising(models.Model):
    image = models.ImageField(
        upload_to='Advertising_image',
        verbose_name='Фотография'
    )
    logo = models.ImageField(
        upload_to='logo+image',
        verbose_name='Фотграфия для соц-сети'
    )
    url = models.URLField(
        verbose_name = 'URL - для insyagram'
    )

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'


class BlogPost(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='BlogPost_image'
    )
    descriptions = models.CharField(
        verbose_name='Название',
        max_length = 255
    )
    profeshion = models.CharField(
        verbose_name='Профессия',
        max_length=255
    )
    about = models.CharField(
        verbose_name='О чем идет новость',
        max_length=255
    )
    data = models.DateTimeField(
        auto_now_add=True, null = True
    )
    zacrep = models.CharField(
        verbose_name='Закрепленные слова',
        max_length=255
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255
    )
    descriptions2 = RichTextField(
        verbose_name='Описание'
    )
    descriptions3 = RichTextField(
        verbose_name='Описание'
    )
    image2 = models.ImageField(
        verbose_name='Фотография',
        upload_to='BlogPost_image2'
    )
    image3 = models.ImageField(
        verbose_name='Фотография',
        upload_to='BlogPost_image3'
    )

    def __str__(self):
        return f'{self.profeshion} - {self.title}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



class Comments(models.Model):
    image = models.ImageField(
        upload_to= 'Comments.image',
        verbose_name='Фотография'
    )
    name = models.CharField(
        verbose_name ='Имя',
        max_length = 255
    )
    comments = models.TextField(
        verbose_name = 'Коментарии'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Коммент'
        verbose_name_plural = 'Коментарии'

class SendComment(models.Model):
    name = models.CharField(
        verbose_name = 'Имя',
        max_length = 255
    )
    email = models.EmailField(
        verbose_name = 'email.com'
    )
    comment = models.TextField(
        verbose_name = 'Отправленный комментарии'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отправленный комментарии'
        verbose_name_plural = 'Отправленный комментарии'