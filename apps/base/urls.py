from django.urls import path
from apps.base import views
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('reservations/', views.reservations, name='reservations')
]