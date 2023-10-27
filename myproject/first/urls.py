from django.urls import path
from .views import IndexView, SecondView
from . import views

app_name = "first"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("second-page/", SecondView.as_view(), name="second-page"),
]
