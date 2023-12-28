from django.urls import path
from . import views
# from django.contrib.auth.decorators import login_required

app_name = "registration"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]
