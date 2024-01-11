from django.contrib import admin
from django.http.request import HttpRequest
from .models import Product, Category

# Register your models here.


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ["name", "price", "category"]
#     ordering = ["name"]

#     def get_prepopulated_field(self, request, obj=None):
#         return {"slug": ("name",)}


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["name", "slug", "parent"]
#     ordering = ["name"]


# admin.site.register(Product)


# admin.site.register(Category)
@admin.register(Product)
class Product_Admin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
        "category",
        "in_stock",
        "slug",

    ]
    ordering = ["name"]

    def get_prepopulated_fields(self, request, obj=None) -> dict[str, tuple[str]]:
        return {"slug": ("name",)}


@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ["name", "slug", "parent"]
    ordering = ["name"]

    def get_prepopulated_fields(self, request, obj=None) -> dict[str, tuple[str]]:
        return {"slug": ("name",)}
