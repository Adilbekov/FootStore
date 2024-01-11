from django.urls import path
from apps.goods import views
urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('shop_detile/<int:id>/', views.shop_detail, name='shop_detile')
]