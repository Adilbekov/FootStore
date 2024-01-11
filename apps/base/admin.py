from django.contrib import admin
from apps.base import models

# Register your models here.

admin.site.register(models.BackImage)
admin.site.register(models.Clients)

class AssPhoneInline(admin.TabularInline):
    model = models.AssPhone

class AssAdmin(admin.ModelAdmin):
    inlines = [AssPhoneInline]

class AssInline(admin.TabularInline):
    model = models.Ass
    extra = 1  # Если нужно избежать дополнительных пустых форм

admin.site.register(models.Ass, AssAdmin)
admin.site.register(models.Contact)
admin.site.register(models.Reservations)
admin.site.register(models.TelegrammBot)