from django.urls import path
from registration import views

app_name = "registration"

urlpatterns = [
    path("register/", views.register_user, name="register"),
]
