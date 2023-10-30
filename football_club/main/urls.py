from django.urls import path, include
from . import views

from .views import Post_News_List, Create_Post_View

# from .views import post_news

app_name = "main"

urlpatterns = [
    # path("", views.home, name="home"),
    # path("", views.post_news, name="posts-news"),
    path("store/", views.store, name="store"),
    path("", Post_News_List.as_view(), name="home"),
    path("add-post/", Create_Post_View.as_view(), name="add-post"),
]
