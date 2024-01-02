from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_data", views.create_data, name="create_data"),
    path("read/", views.read, name="read"),
]
