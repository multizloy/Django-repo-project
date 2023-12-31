from datetime import timezone
from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic.list import MultipleObjectMixin
from store.models import Item, Category
from store.filters import Product_Filter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# предметный лист
class Item_List(generic.ListView):
    template_name = "store/item_list.html"
    # form_class = Item
    model = Item
    context_object_name = "items"
    paginate_by = 6

    # контекст для навбара
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all().order_by("name")
        # поиск товара?
        filters = Product_Filter(self.request.GET, queryset=Item.objects.all())
        paginator = Paginator(filters.qs, 6)
        page = self.request.GET.get("page")
        paged_listings = paginator.get_page(page)

        context["categories"] = categories
        context["filters"] = filters
        context["paginator_filter"] = paged_listings
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
    paginate_by = 1

    # контекст для навбара
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all().order_by("name")
        items = Item.objects.all().filter(category_id=self.kwargs["pk"])
        context["items"] = items
        context["categories"] = categories
        return context


def search_item(request):
    search_text = request.POST.get("search")
    # icontains для того, чтобы было всеравно на шрифт
    results = Item.objects.filter(name__icontains=search_text)
    context = {"results": results}
    return render(request, "store/search_results.html", context)
