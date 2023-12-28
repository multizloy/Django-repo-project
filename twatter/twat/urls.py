from django.urls import include, path
from . import views

app_name = "twat"

urlpatterns = [
    path("", views.index, name="index"),
]
