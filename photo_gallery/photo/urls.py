from django.urls import path
from . import views

app_name = "photo"
urlpatterns = [
    path("", views.index, name="index"),
]
