from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from django.views import generic

from fc_mltz import settings
from registration.models import User

from .forms import Post_News_Form
from .mixin import LoginRequiredMixin
from .models import PostNews

# Create your views here.


def home(request):
    return render(request, "main/home.html")


# выводим лист всех постов на сайте
class Post_News_List(generic.ListView):
    model = PostNews
    template_name = "main/list_post.html"
    context_object_name = "posts"
    # paginate_by = 6


# создаем класс для создания новых постов на сайте
class Create_Post_View(LoginRequiredMixin, generic.CreateView):
    template_name = "main/add_post.html"
    model = PostNews
    fields = ["title", "text"]
    # form_class = Post_News_Form

    success_url = reverse_lazy("main:list-post")
    login_url = reverse_lazy("registration:login")

    # автоматически сохряняет автора статьи в базу данных по авторизированному пользователю в система(автор_ид)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # передает сохраненные слаги в ссылки?
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


# просмотр отдельных постов
class View_Post_View(LoginRequiredMixin, generic.DetailView):
    template_name = "main/view_post.html"
    slug_url_kwarg = "slug"
    model = PostNews
    context_object_name = "post"

    # открываем деталь вбю отдельной статьи
    def get_object(self, queryset=None):
        return get_object_or_404(PostNews, slug=self.kwargs[self.slug_url_kwarg])


class Update_Post_View(LoginRequiredMixin, generic.UpdateView):
    template_name = "main/update_post.html"
    form_class = Post_News_Form
    context_object_name = "post"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("main:list-post")
    login_url = reverse_lazy("registration:login")

    def get_object(self, queryset=None):
        return get_object_or_404(PostNews, slug=self.kwargs[self.slug_url_kwarg])


class Delete_Post_View(LoginRequiredMixin, generic.DeleteView):
    template_name = "main/delete_post.html"

    context_object_name = "post"
    success_url = reverse_lazy("main:list-post")

    def get_queryset(self) -> QuerySet[Any]:
        return PostNews.objects.all()

