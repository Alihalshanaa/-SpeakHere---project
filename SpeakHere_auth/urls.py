from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup , name='signup'),
    path('handlelogin/', views.handlelogin , name='handlelogin'),
    path('handlelogout/', views.handlelogout , name='handlelogout'),
]