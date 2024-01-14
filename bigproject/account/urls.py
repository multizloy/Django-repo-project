from django.shortcuts import render
from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    # Registration and verification
    path("register/", views.register_user, name="register"),
    path(
        "email-verification-sent/",
        lambda request: render(request, "account/email-verification-sent.html"),
        name="email-verification-sent",
    ),
    # login
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    # dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile-management/", views.profile_management, name="profile-management"),
    path("profile-delete/", views.profile_delete, name="profile-delete"),
]
