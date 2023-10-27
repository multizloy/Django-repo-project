from django.urls import path
from .views import LoginView

app_name = "registration"

urlpatterns = [
    path("register/", LoginView.as_view(), name="register"),
]
