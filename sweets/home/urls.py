from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('order', views.order, name='order'),
    path('calculate_total', views.calculate_total, name='calculate_total'),
    path('showCart', views.showCart, name='showCart'),
    path('user_detail', views.user_detail, name='user_detail')
]
