from django import forms

from .models import Shipping_Address, Order, Order_Item


class Shipping_Address_Form(forms.ModelForm):
    class Meta:
        model = Shipping_Address
        fields = [
            "email",
            "address",
            "city",
            "state",
            "zip_code",
            "phone_number",
        ]
        exclude = (
            "user",
            "is_default",
        )
