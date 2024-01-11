from django.contrib import admin
from apps.menu import models
# Register your models here.
admin.site.register(models.SetFamily)
admin.site.register(models.SetCouple)
admin.site.register(models.SetIndivudal)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

admin.site.register(models.FootBurger)
admin.site.register(models.FootPasta)
admin.site.register(models.FootPizza)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

admin.site.register(models.DessertCake)
admin.site.register(models.DessertIceCream)
admin.site.register(models.DessertSnake)


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

admin.site.register(models.JuiceCoffee)
admin.site.register(models.JuiceFruitJuice)