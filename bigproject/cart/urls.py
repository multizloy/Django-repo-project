from django.urls import path, include
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_view, name="cart-view"),
    path("add/", views.cart_add, name="add_to_cart"),
    path("delete/", views.cart_delete, name="delete_from_cart"),
    path("update/", views.cart_update, name="update_cart"),
]
