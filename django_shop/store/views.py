import json
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import Product, Cart, Cart_Item
from django.contrib import messages

# Create your views here.


def index(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    context = {"products": products, "cart": cart}
    return render(request, "store/index.html", context)


def cart(request):
    cart = None
    cart_items = []
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cart_items = Cart_Item.objects.filter(cart=cart)

    context = {"cart": cart, "cart_items": cart_items}
    return render(request, "store/cart.html", context)


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cart_item, created = Cart_Item.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()

        num_of_items = cart.num_of_items
        print(cart_item)
    return JsonResponse(num_of_items, safe=False)


def remove_from_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    if request.POST.get("delete") == "post":
        # Removes a product from the cart.
        # Gets the product ID from the POST data.
        cart_item = Cart_Item.objects.get(cart=cart, product=product)
        cart_item.delete()

    return render(request, "store/cart.html", {"cart": cart})



def confirm_payment(request, pk):
    cart = Cart.objects.get(pk=pk)
    cart.completed = True
    cart.save()
    messages.success(request, "Payment Confirmed")
    return redirect("store:index")
