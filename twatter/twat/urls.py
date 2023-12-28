from django.urls import include, path
from . import views

app_name = "twat"

urlpatterns = [
    path("", views.index, name="index"),
    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>/", views.profile, name="profile"),
]
