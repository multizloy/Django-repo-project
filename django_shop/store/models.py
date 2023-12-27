import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    picture = models.ImageField(upload_to="static/images/products", default="")

    def __str__(self) -> str:
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        total = 0
        for item in self.cart_item_cart.all():
            total += item.price
        return total
    
    @property
    def num_of_items(self):
        total_quantity = 0
        for quantity in  self.cart_item_cart.all():
            total_quantity += quantity.quantity
        return total_quantity
        
        
    
class Cart_Item(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_item_cart"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="cart_item_product"
    )
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product.name
    
    @property
    def price(self):
        new_price = self.product.price * self.quantity
        return new_price
