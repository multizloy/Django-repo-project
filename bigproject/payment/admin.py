from django.contrib import admin
from .models import Shipping_Address, Order, Order_Item


# Register your models here.
@admin.register(Shipping_Address)
class Shipping_Address_Admin(admin.ModelAdmin):
    list_display = [
        "user",
        "email",
        "address",
        "city",
        "state",
        "zip_code",
        "phone_number",
        "is_default",
    ]
    ordering = ["user"]


@admin.register(Order)
class Order_Admin(admin.ModelAdmin):
    list_display = [
        "user",
        "shipping_address",
        "amount",
        "created",
        "updated",
    ]
    ordering = ["user"]


@admin.register(Order_Item)
class Order_Item_Admin(admin.ModelAdmin):
    list_display = [
        "order",
        "product",
        "price",
        "quantity",
        "user",
    ]
