from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', authenticate,name="login"),
    path('register', register, name="register"),
    path('logout', logout, name="logout"),
]
