from django.db import models

# Create your models here.

# class Setting(models.Model):

class BackImage(models.Model):
    image1 = models.ImageField(
        verbose_name='Фотография для заднего фона',
        upload_to='BackImage_image1'
    )
    image2 = models.ImageField(
        verbose_name='Фотография для заднего фона',
        upload_to='BackImage_image2'
    )
    image3 = models.ImageField(
        verbose_name='Фотография для заднего фона',
        upload_to='BackImage_image3'
    )
    image4 = models.ImageField(
        verbose_name='Фотография для заднего фона',
        upload_to='BackImage_image4'
    )
    image5 = models.ImageField(
        verbose_name='Фотография для заднего фона',
        upload_to='BackImage_image5'
    )
    image6 = models.ImageField(
        verbose_name='Фотография для заднего фона',
        upload_to='BackImage_image6'
    )

    class Meta:
        verbose_name = 'Фотография заднего фона'
        verbose_name_plural = 'Фотографии заднего фона'



class Clients(models.Model):
    photo = models.ImageField(
        verbose_name='Фотография данной персоны',
        upload_to='Clients_image'
    )
    name = models.CharField(
        verbose_name = 'Имя',
        max_length = 255
    )
    profession = models.CharField(
        verbose_name = 'Должность',
        max_length = 255
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )

    def __str__(self):
        return f'{self.name} - {self.profession}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Ass(models.Model):
    logo = models.ImageField(
        upload_to='Ass_logo',
        verbose_name='Логотип'
    )
    descriptions = models.TextField(
        verbose_name = 'Описание'
    )
    url_instagram = models.URLField(
        verbose_name = 'URL - Instagram'
    )
    url_internet = models.URLField(
        verbose_name = 'URL - ...'
    )
    url_twitter = models.URLField(
        verbose_name = 'URL - Twitter'
    )
    url_you_tube = models.URLField(
        verbose_name = 'URL - You Tube'
    )
    adres = models.CharField(
        verbose_name = 'Адрес',
        max_length = 255
    )
    email = models.EmailField(
        verbose_name = 'email.com'
    )

    def __str__(self):
        return self.descriptions
    
    class Meta:
        verbose_name = 'Основная настройка'
        verbose_name_plural = 'Основные настройки'

# Inline bottons
class AssPhone(models.Model):
    settings=models.ForeignKey(Ass, related_name='options', on_delete=models.CASCADE)
    phone=models.CharField(
        verbose_name='Телефонные номера',
        max_length=255
    )


class Contact(models.Model):
    name = models.CharField(
        verbose_name = 'Имя',
        max_length = 255
    )
    email = models.CharField(
        verbose_name = 'Email.com',
        max_length = 255
    )
    subject = models.CharField(
        verbose_name = 'Предмет',
        max_length = 255
    )
    message = models.CharField(
        verbose_name = 'Сообшение: ',
        max_length = 255
    )

    def _str__(self):
        return f'{self.name} - {self.email}'
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Reservations(models.Model):
    name = models.CharField(
        verbose_name = 'Имя',
        max_length = 255
    )
    email = models.EmailField(
        verbose_name = 'email.com'
    )
    person = models.CharField(
        verbose_name = 'Количество людей',
        max_length = 255
    )
    phone = models.CharField(
        verbose_name = 'Телефонный номер',
        max_length = 255
    )
    data = models.CharField(
        verbose_name = 'Дата',
        max_length = 255
    )
    time = models.CharField(
        verbose_name = 'Дата',
        max_length = 255
    )
    message = models.TextField(
        verbose_name = 'Сообшение'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'


class TelegrammBot(models.Model):
    name = models.CharField(
        verbose_name = 'Имя',
        max_length = 255
    )
    email = models.EmailField(
        verbose_name = 'email.com'
    )
    subject = models.CharField(
        verbose_name = 'Услуга',
        max_length = 255
    )
    message = models.TextField(
        verbose_name = 'Услуга',
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Обратная связь - Telegram'
        verbose_name_plural = 'Обратная связь - Telegram'