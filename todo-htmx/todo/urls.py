# from django import views
from django.shortcuts import render, redirect

from django.urls import path
from .views import index
from todo import views

app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("status/<int:pk>/", views.status, name="status"),
]
