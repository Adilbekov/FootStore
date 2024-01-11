from django.urls import path
from apps.secondary import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('blogs/', views.blog, name='blog'),
    path('blog_detiles/<int:id>/', views.blog_detiles, name='blog_detiles'),
    path('404/', views.bag, name='404')
]