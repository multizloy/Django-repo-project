from django.shortcuts import render
from django.views import generic

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "first/index.html"

    def index(request):
        return render(request, "first/index.html")


class SecondView(generic.TemplateView):
    template_name = "first/second-page.html"

    def second_page(request):
        return render(request, "first/second-page.html")
