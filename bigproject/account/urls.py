from django.shortcuts import render
from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    # Registration and verification
    path("register/", views.register_user, name="register"),
    path(
        "email_verification/",
        lambda request: render(request, "account/email/email_verification.html"),
        name="email_verification",
    ),
    #login
    path("login/", views.login_user, name="login"),
    # path("logout/", views.logout_user, name="logout"),
]
