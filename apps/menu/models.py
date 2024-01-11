from django.db import models

# Create your models here.

class SetFamily(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Сет для семьи'
        verbose_name_plural = 'Сет для семьи'


class SetCouple(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Сет для пар'
        verbose_name_plural = 'Сет для пары'


class SetIndivudal(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Сет для индивидуальных'
        verbose_name_plural = 'Сет для индивидуальных'

# ::::::::::::::::::::::::::Aman-loh::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        

class FootBurger(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Fast-Food: Бургер'
        verbose_name_plural = 'Fast-Food: Бургеры'


class FootPasta(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Fast-Food: Паста'
        verbose_name_plural = 'Fast-Food: Пасты'

class FootPizza(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Fast-Food: Питца'
        verbose_name_plural = 'Fast-Food: Питцы'



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


class DessertSnake(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Десерт: Snake'
        verbose_name_plural = 'Десерты: Snake'

class DessertIceCream(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Десерт: Мороженое'
        verbose_name_plural = 'Десерты: Мороженое'


class DessertCake(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Десерт торт'
        verbose_name_plural = 'Десерты торты'


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        


class JuiceFruitJuice(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Напитки: Фруктовый сок'
        verbose_name_plural = 'Напитки: Фруктовый сок'


class JuiceCoffee(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='SetFamily_image'
    )
    name = models.CharField(
        verbose_name = 'Название',
        max_length = 255
    )
    description = models.TextField(
        verbose_name = 'Описание'
    )
    old_price = models.CharField(
        verbose_name = 'Прошлая цена',
        max_length = 255
    )
    price = models.CharField(
        verbose_name = 'Цена',
        max_length = 255
    )

    def __str__(self):
        return f'{self.name} - {self.price}'
    
    class Meta:
        verbose_name = 'Напитки:  Кофе'
        verbose_name_plural = 'Напитки: Кофе'