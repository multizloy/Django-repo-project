from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from .models import UserProfile

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import (
    MyUserCreationForm,
    User_Profile_Update_Form,
)


# Create your views here.


class CreateRegisterView(generic.CreateView):
    form_class = MyUserCreationForm
    template_name = "registration/register.html"

    success_url = reverse_lazy("registration:login")


class Dashboard(generic.ListView):
    template_name = "registration/dashboard.html"
    form_class = User_Profile_Update_Form
    context_object_name = "profiles"
    success_url = reverse_lazy("main:home")
    login_url = reverse_lazy("registration:login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        # user = self.request.user
        return UserProfile.objects.filter()
