from django.shortcuts import render
from django.views import generic

from store.models import Item

# Create your views here.



class Item_List(generic.ListView):
    template_name = "store/item_list.html"
    form_class = Item
    context_object_name = "items"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        me = self.request.user
        # profile = UserProfile.objects.filter(
        #     username=me, email=me, first_name=me, last_name=me
        # )
        return Item.objects.all()
