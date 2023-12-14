from django.urls import path, include
from .views import *
from . import views

app_name = "cart"


urlpatterns = [
    # path("", Cart_List.as_view(), name="cart-list"),
    # path("add-cart/", Add_Cart_List.as_view(), name="cart-add"),
    # path("update-cart/", Update_Cart_List.as_view(), name="cart-update"),
    # path("delete-cart/", Delete_Cart_List.as_view(), name="cart-delete"),
    # path("", views.cart_summary, name="cart-list"),
    path("", Cart_List.as_view(), name="cart-list"),
    path("add-cart/", views.add_cart_summary, name="cart-add"),
    path("update-cart/", views.update_cart_summary, name="cart-update"),
    path("delete-cart/", views.delete_cart_summary, name="cart-delete"),
]
