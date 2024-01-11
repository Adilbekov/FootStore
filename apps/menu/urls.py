from django.urls import path
from apps.menu import views
urlpatterns = [
    path('menu/', views.menu, name='menu'),
]