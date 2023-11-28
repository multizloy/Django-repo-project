from django.shortcuts import render
from django.views import generic

from store.models import Item, Category

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


class Category_Shorts(generic.ListView):
    template_name = "store/category_shorts.html"
    form_class = Item
    context_object_name = "shorts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Item.objects.filter(category_id=5)


class Category_Hats(generic.ListView):
    template_name = "store/category_hats.html"
    form_class = Item
    context_object_name = "hats"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Item.objects.filter(category_id=6)


class Category_Boots(generic.ListView):
    template_name = "store/category_boots.html"
    form_class = Item
    context_object_name = "boots"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Item.objects.filter(category_id=4)


class Category_Tshirts(generic.ListView):
    template_name = "store/category_tshirts.html"
    form_class = Item
    context_object_name = "tshirts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Item.objects.filter(category_id=2)


class Category_Skarfs(generic.ListView):
    template_name = "store/category_skarfs.html"
    form_class = Item
    context_object_name = "skarfs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Item.objects.filter(category_id=3)


class Category_Balls(generic.ListView):
    template_name = "store/category_balls.html"
    form_class = Item
    context_object_name = "balls"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Item.objects.filter(category__name="Мячи")
