from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.book, name='book'),
    path('login', views.loginuser, name='login'),
    path('home', views.home, name='home')
]