from django.shortcuts import render
from django.views import generic

from store.models import Item, Category


# предметный лист
class Item_List(generic.ListView):
    template_name = "store/item_list.html"
    # form_class = Item
    model = Item
    context_object_name = "items"


# страница для отдельных страниц вещей в магазине
class Item_Detail(generic.DetailView):
    template_name = "store/item_detail.html"
    model = Item
    context_object_name = "item"


# классы для категорий товаров
class Category_Shorts(generic.ListView):
    template_name = "store/category_shorts.html"
    model = Item
    context_object_name = "shorts"

    def get_queryset(self):
        return Item.objects.filter(category_id=5)


class Category_Hats(generic.ListView):
    template_name = "store/category_hats.html"
    model = Item
    context_object_name = "hats"

    def get_queryset(self):
        return Item.objects.filter(category_id=6)


class Category_Boots(generic.ListView):
    template_name = "store/category_boots.html"
    model = Item
    context_object_name = "boots"

    def get_queryset(self):
        return Item.objects.filter(category_id=4)


class Category_Tshirts(generic.ListView):
    template_name = "store/category_tshirts.html"
    model = Item
    context_object_name = "tshirts"

    def get_queryset(self):
        return Item.objects.filter(category_id=2)


class Category_Skarfs(generic.ListView):
    template_name = "store/category_skarfs.html"
    model = Item
    context_object_name = "skarfs"

    def get_queryset(self):
        return Item.objects.filter(category_id=3)


class Category_Balls(generic.ListView):
    template_name = "store/category_balls.html"
    model = Item
    context_object_name = "balls"

    def get_queryset(self):
        return Item.objects.filter(category__name="Мячи")
