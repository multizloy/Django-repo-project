from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from .forms import MyUserCreationForm

# Create your views here.


# class RegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = "registration/register.html"
#     success_url = reverse_lazy("registration:login")


class CreateRegisterView(generic.CreateView):
    form_class = MyUserCreationForm
    template_name = "registration/register.html"

    success_url = reverse_lazy("registration:login")
