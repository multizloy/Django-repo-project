from django.urls import include, path
from . import views

app_name = "twat"

urlpatterns = [
    path("", views.index, name="index"),
    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>/", views.profile, name="profile"),
    path("profile/edit/", views.profile_edit, name="profile_edit"),
    path("profile/followers/<int:pk>/", views.followers, name="followers"),
    path("twat_like/<int:pk>/", views.twat_like, name="twat_like"),
    path("twat_share/<int:pk>/", views.twat_share, name="twat_share"),
    path("unfollow/<int:pk>/", views.unfollow, name="unfollow"),
    path("follow/<int:pk>/", views.unfollow, name="follow"),
]
