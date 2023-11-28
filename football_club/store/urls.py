from django.urls import path, include
from .views import *

app_name = "store"


urlpatterns = [
    path("", Item_List.as_view(), name="item-list"),
    path("category-shorts/", Category_Shorts.as_view(), name="category-shorts"),
    path("category-hats/", Category_Hats.as_view(), name="category-hats"),
    path("category-boots/", Category_Boots.as_view(), name="category-boots"),
    path("category-tshirts/", Category_Tshirts.as_view(), name="category-tshirts"),
    path("category-skarfs/", Category_Skarfs.as_view(), name="category-skarfs"),
    path("category-balls/", Category_Balls.as_view(), name="category-balls"),
]
