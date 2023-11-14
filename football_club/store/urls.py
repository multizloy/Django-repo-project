from django.urls import path, include
from .views import *

app_name = "store"


urlpatterns = [
    path("", Item_List.as_view(), name="item-list"),
]
