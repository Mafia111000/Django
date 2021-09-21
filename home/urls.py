from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.first, name='blank'),
    path('about/', views.about, name='about'),
    path('Home/', views.Home, name='home'),
]