from datetime import timezone
from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views import generic

from store.models import Item, Category


# предметный лист
class Item_List(generic.ListView):
    template_name = "store/item_list.html"
    # form_class = Item
    model = Item
    context_object_name = "items"

    # контекст для навбара
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all().order_by("name")
        context["categories"] = categories
        return context


# страница для отдельных страниц вещей в магазине
class Item_Detail(generic.DetailView):
    template_name = "store/item_detail.html"
    model = Item
    context_object_name = "item"

    # контекст для навбара
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all().order_by("name")
        context["categories"] = categories
        return context


# cоздаем страницу для предметов одной категории и выводим эти предметы
class Category_Detail(generic.DetailView):
    template_name = "store/category_detail.html"
    model = Category
    context_object_name = "category"
    slug_url_kwarg = "slug_cat"

    # def get_queryset(self):
    #     qs = super(Item, self).get_queryset()
    #     return qs

    # контекст для навбара
    def get_context_data(self, **kwargs):
        i = self.kwargs["slug_cat"]
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all().order_by("name")
        items = Item.objects.all().filter(self.item.category == self.kwargs["slug_cat"])
        # item = Item.objects.all().filter(name=self.kwargs["slug_cat"])
        # item = Item.objects.all().filter(category_id=self.kwargs["slug"])
        context["items"] = items
        # context["items"] = item
        context["categories"] = categories
        print(item)
        print(i)
        return context
