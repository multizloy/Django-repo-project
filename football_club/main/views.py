from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from django.views import generic
from .models import PostNews
from .forms import Post_News_Form
from .mixin import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, "main/home.html")


@login_required(login_url="main:home")
def store(request):
    return render(request, "main/store.html")


class Post_News_List(generic.ListView):
    form_class = Post_News_Form
    template_name = "main/home.html"
    context_object_name = "post"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        # user = self.request.user
        return PostNews.objects.filter()


class Create_Post_View(LoginRequiredMixin, generic.CreateView):
    template_name = "main/add_post.html"
    form_class = Post_News_Form
    success_url = reverse_lazy("main:home")
    login_url = reverse_lazy("registration:login")
