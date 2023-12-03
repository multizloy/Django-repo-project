from django.urls import path, include
from .views import *

app_name = "store"


urlpatterns = [
    path("", Item_List.as_view(), name="item-list"),
    path("item-detail/<int:pk>/", Item_Detail.as_view(), name="item-detail"),
    path("category/<int:pk>/", Category_Detail.as_view(), name="category"),
]
