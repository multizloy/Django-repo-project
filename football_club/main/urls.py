from django.urls import path, include
from . import views

from .views import (
    Post_News_List,
    Create_Post_View,
    View_Post_View,
    Update_Post_View,
    Delete_Post_View,
)

# from .views import post_news

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("list-post/", Post_News_List.as_view(), name="list-post"),
    path("add-post/", Create_Post_View.as_view(), name="add-post"),
    path("list-post/<str:slug>/", View_Post_View.as_view(), name="view-post"),
    # path("list-post/<int:pk>/", View_Post_View.as_view(), name="view-post"),
    # path("list-post/update/<int:pk>/", Update_Post_View.as_view(), name="update-post"),
    #  слаг на странице просмотра отдельной статьи
    path(
        "list-post/update/<str:slug>/", Update_Post_View.as_view(), name="update-post"
    ),
    path("list-post/delete/<str:slug>", Delete_Post_View.as_view(), name="delete-post"),
]
htmx_urlpattern = [
    # path(
    #     "delete-post/delete/<str:slug>", Delete_Post_View.as_view(), name="delete-post"
    # ),
# """     path("list-post/delete/<int:pk>", Delete_Post_View.as_view(), name="delete"),
# ] """
]
urlpatterns += htmx_urlpattern
