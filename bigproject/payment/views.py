from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
from cart.cart import Cart
from .models import Shipping_Address, Order, Order_Item
from .forms import Shipping_Address_Form


@login_required(login_url="account:login")
def shipping(request):
    try:
        shipping_address = Shipping_Address.objects.get(
            user=request.user, is_default=True
        )
    except Shipping_Address.DoesNotExist:
        shipping_address = None

    form = Shipping_Address_Form(instance=shipping_address)
    if request.method == "POST":
        form = Shipping_Address_Form(request.POST, instance=shipping_address)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.user = request.user
            shipping_address.is_default = True
            shipping_address.save()
            return redirect("account:dashboard")
    return render(request, "payment/shipping.html", {"form": form})


def checkout(request):
    if request.user.is_authenticated:
        shipping_address = get_object_or_404(Shipping_Address, user=request.user)
        if shipping_address:
            return render(
                request, "payment/checkout.html", {"shipping_address": shipping_address}
            )
    return render(request, "payment/checkout.html")


def complete_order(request):
    if request.POST.get("action") == "payment":
        email = request.POST.get("email")
        street_address = request.POST.get("street_address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")

        cart = Cart(request)
        total_price = cart.get_total_price()

        shipping_address, _ = Shipping_Address.objects.get_or_create(
            user=request.user,
            defaults={
                "email": email,
                "street_address": street_address,
                "city": city,
                "state": state,
                "zip": zip,
            },
        )

    if request.user.is_authenticated:
        order = Order.objects.create(
            user=request.user, shipping_address=shipping_address, amount=total_price
        )

        for item in cart:
            Order_Item.objects.create(
                order=order,
                product=item["product"],
                price=item["price"],
                quantity=item["qty"],
                user=request.user,
            )
    else:
        order = Order.objects.create(
            shipping_address=shipping_address, amount=total_price
        )

        for item in cart:
            Order_Item.objects.create(
                order=order,
                product=item["product"],
                price=item["price"],
                quantity=item["qty"],
            )

    return JsonResponse({"success": True})


def payment_success(request):
    for key in list(request.session.keys()):
        if key.startswith("cart_"):
            del request.session[key]
    return render(request, "payment/payment_success.html")


def payment_fail(request):
    return render(request, "payment/payment_fail.html")
