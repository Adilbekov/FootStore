from django.contrib import admin
from apps.secondary import models
# Register your models here.

admin.site.register(models.Slide)
admin.site.register(models.Quality)
admin.site.register(models.Foot)
admin.site.register(models.Advertising)
admin.site.register(models.BlogPost)
admin.site.register(models.Comments)
admin.site.register(models.SendComment)