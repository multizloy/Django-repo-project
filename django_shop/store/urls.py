from . import views
from django.urls import path

app_name = "store"

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("add_to_cart/", views.add_to_cart, name="add"),
    path("remove_from_cart/", views.remove_from_cart, name="remove"),
    path("confirm_payment/<int:pk>/", views.confirm_payment, name="confirm"),
]
