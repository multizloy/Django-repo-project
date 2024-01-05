from django.urls import path
from .views import Posts

# app_name = "rest_api"

urlpatterns = [
    path("posts/", Posts, name="posts"),
]
