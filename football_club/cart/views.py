from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic
import requests

from store.models import Category, Item
from .cart import Cart
from django.http import JsonResponse

# Create your views here.


class Cart_List(generic.ListView):
    def dispatch(self, request, *args, **kwargs):
        cart = Cart(request)  # Get the cart object
        cart_items = cart.get_item()  # Call the get_prods function
        # quantities = cart.get_quants()  # Call the get_quants function
        # context = {"cart_products": cart_products, "quantities": quantities}
        categories = Category.objects.all().order_by("name")
        context = {"cart_items": cart_items, "categories": categories}
        return render(request, "cart/cart_list.html", context)


# class Cart_List(generic.TemplateView):

#     def dispatch(self, request, *args, **kwargs):
#         cart = Cart(request)  # Get the cart object
#         cart_items = cart.get_item()  # Call the get_prods function
#         # quantities = cart.get_quants()  # Call the get_quants function
#         # context = {"cart_products": cart_products, "quantities": quantities}
#         context = {"cart_items": cart_items}
#         return render(request, "cart/cart_list.html", context)
#         # контекст для навбара

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         categories = Category.objects.all().order_by("name")
#         context["categories"] = categories
#         return context


# class Add_Cart_List(generic.CreateView):
#     pass


# class Update_Cart_List(generic.UpdateView):
#     pass


# class Delete_Cart_List(generic.DeleteView):
#     pass


# def cart_summary(request):
#     # Get the cart
#     cart = Cart(request)
#     cart_products = cart.get_item
#     return render(request, "cart/cart_list.html", {"cart_products": cart_products})


def add_cart_summary(request):
    # Get cart
    cart = Cart(request)
    # test for post
    if request.POST.get("action") == "post":
        # Get stuff
        item_id = request.POST.get("item_id")
        # lookup item in DB
        item = get_object_or_404(Item, id=item_id)

        # save ot session
        cart.add(item=item)
        # Get cart quantity
        cart_quantity = cart.__len__()

        # return Response
        # response = JsonResponse({"Item Name: ": item.name})
        response = JsonResponse({"qty": cart_quantity})
        return response


def update_cart_summary(request):
    pass


def delete_cart_summary(request):
    pass
