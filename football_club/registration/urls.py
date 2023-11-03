from django.urls import path, include, reverse_lazy


# from .views import RegisterView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .views import *

app_name = "registration"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", CreateRegisterView.as_view(), name="register"),
    path(
        "reset-password/",
        PasswordResetView.as_view(),
        name="password-reset",
    ),
    path(
        "password-reset-done/",
        PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password-reset-done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # path("", include("django.contrib.auth.urls")),
    path("dashboard/", Dashboard.as_view(), name="dashboard"),
]
