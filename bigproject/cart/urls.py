from django.urls import path, include
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_view, name="cart-view"),
    path("add/", views.cart_add, name="add_to_cart"),
    # path("category/<slug:slug>/", views.category_list, name="category-list"),
]
