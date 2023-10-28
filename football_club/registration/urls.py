from django.urls import path
from . import views
from .views import RegisterView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)

app_name = "registration"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    # path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
]
