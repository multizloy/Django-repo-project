from django.urls import path, include
from .views import *

app_name = "cart"


urlpatterns = [
    path("", Cart_List.as_view(), name="cart-list"),
    path("add-cart/", Add_Cart_List.as_view(), name="cart-add"),
    path("update-cart/", Update_Cart_List.as_view(), name="cart-update"),
    path("delete-cart/", Delete_Cart_List.as_view(), name="cart-delete"),
]
