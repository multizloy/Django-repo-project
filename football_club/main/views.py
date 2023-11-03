from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from django.views import generic

from .forms import Post_News_Form
from .mixin import LoginRequiredMixin
from .models import PostNews

# Create your views here.


def home(request):
    return render(request, "main/home.html")


@login_required(login_url="registration:login")
def store(request):
    return render(request, "main/store.html")


class Post_News_List(generic.ListView):
    form_class = Post_News_Form
    template_name = "main/list_post.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        # user = self.request.user
        return PostNews.objects.filter()


class Create_Post_View(LoginRequiredMixin, generic.CreateView):
    template_name = "main/add_post.html"
    form_class = Post_News_Form
    success_url = reverse_lazy("main:list-post")
    login_url = reverse_lazy("registration:login")


class View_Post_View(LoginRequiredMixin, generic.DetailView):
    template_name = "main/view_post.html"
    form_class = Post_News_Form
    context_object_name = "posts"

    success_url = reverse_lazy("main:view-post")

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            queryset = PostNews.objects.all()

        return queryset


class Update_Post_View(LoginRequiredMixin, generic.UpdateView):
    template_name = "main/update_post.html"
    form_class = Post_News_Form
    context_object_name = "posts"
    success_url = reverse_lazy("main:list-post")
    login_url = reverse_lazy("registration:login")

    def get_queryset(self) -> QuerySet[Any]:
        return PostNews.objects.all()


class Delete_Post_View(LoginRequiredMixin, generic.DeleteView):
    template_name = "main/delete_post.html"
    queryset = PostNews.objects.all()
    context_object_name = "posts"
    success_url = reverse_lazy("main:list-post")

    def get_queryset(self):
        return PostNews.objects.all()


# Создадим Личный кабинет
