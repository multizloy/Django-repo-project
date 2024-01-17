from django.shortcuts import render
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

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
    # password reset
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password/password_reset.html",
            email_template_name="account/password/password_reset_email.html",
            success_url=reverse_lazy("account:password-reset-done"),
        ),
        name="password-reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password/password_reset_done.html",
        ),
        name="password-reset-done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password/password_reset_confirm.html",
            success_url=reverse_lazy("account:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password/password_reset_complete,html"
        ),
        name="password_reset_complete",
    ),
]
