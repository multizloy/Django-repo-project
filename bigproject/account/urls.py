from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("email_verification/", views.email_verification, name="email_verification"),
]
