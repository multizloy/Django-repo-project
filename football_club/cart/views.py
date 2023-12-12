from django.shortcuts import render, get_object_or_404
from django.views import generic

from store.models import Item
from .cart import Cart
from django.http import JsonResponse

# Create your views here.


# class Cart_List(generic.ListView):
#     template_name = "cart/cart_list.html"
#     model = Item


# class Add_Cart_List(generic.CreateView):
#     pass


# class Update_Cart_List(generic.UpdateView):
#     pass


# class Delete_Cart_List(generic.DeleteView):
#     pass


def cart_summary(request):
    return render(request, "cart/cart_list.html", {})


def add_cart_summary(request):
    # Get cart
    cart = Cart(request)
    # test for post
    if request.POST.get("action") == "post":
        # Get stuff
        item_id = int(request.POST.get("item.id"))
        # lookup item in DB
        item = get_object_or_404(Item, id=item_id)
        print(item_id)
        # save ot session
        cart.add(item=item)

        # return Response
        response = JsonResponse({"Item Name: ": item.name})
        return response


def update_cart_summary(request):
    pass


def delete_cart_summary(request):
    pass
