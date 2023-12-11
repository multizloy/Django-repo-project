from django.shortcuts import render
from django.views import generic

from store.models import Item

# Create your views here.


class Cart_List(generic.ListView):
    template_name = "cart/cart_list.html"
    model = Item


class Add_Cart_List(generic.CreateView):
    pass


class Update_Cart_List(generic.UpdateView):
    pass


class Delete_Cart_List(generic.DeleteView):
    pass
