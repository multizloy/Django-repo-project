from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

# Create your views here.


class LoginView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("register")
    template_name = "registration/register.html"
