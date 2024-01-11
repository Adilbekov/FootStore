from django.contrib import admin
from apps.goods import models
# Register your models here.

admin.site.register(models.Donuts)
admin.site.register(models.Bread)
admin.site.register(models.Cake)
admin.site.register(models.LowPrice)