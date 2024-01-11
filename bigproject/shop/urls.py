from django.urls import path, include
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.products_view, name="products"),
    path("<slug:slug>/", views.products_detail_view, name="products_detail"),
    path("category/<slug:slug>/", views.category_list, name="category_list"),
]
