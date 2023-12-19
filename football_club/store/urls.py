from django.urls import path, include
from .views import *
from . import views

app_name = "store"


urlpatterns = [
    path("", Item_List.as_view(), name="item-list"),
    path(
        "category/<str:cat_name>/<str:item_name>/<int:pk>/",
        Item_Detail.as_view(),
        name="item-detail",
    ),
    path(
        "category/<slug:slug_cat>/<int:pk>",
        Category_Detail.as_view(),
        name="category",
    ),
]

htmx_urlpatterns = [path("search-item/", views.search_item, name="search-item")]
urlpatterns += htmx_urlpatterns
