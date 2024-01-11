from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Product_Proxy

# Create your views here.


def products_view(request):
    products = Product_Proxy.objects.all()
    return render(request, "shop/products.html", {"products": products})


def products_detail_view(request, slug):
    product = get_object_or_404(Product_Proxy, slug=slug)
    return render(request, "shop/products_detail.html", {"product": product})


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product_Proxy.objects.filter(category=category)
    context = {"category": category, "products": products}
    return render(request, "shop/category_list.html", context)
