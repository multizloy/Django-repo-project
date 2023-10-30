from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import MyUserCreationForm


# Create your views here.


class CreateRegisterView(generic.CreateView):
    form_class = MyUserCreationForm
    template_name = "registration/register.html"

    success_url = reverse_lazy("registration:login")
