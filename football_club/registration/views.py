from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


# def registerPage(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#         else:
#             return redirect("registration/register.html")
#     else:
#         context = {"form": form}
#         return render(request, "registration/register.html", context)


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, user)
#         if user is not None:
#             login(request, user)
#             return redirect("main/home.html")
#         else:
#             return redirect("registration/register.html")
#     else:
#         return render(request, "registration/register.html")


# def login(request):
#     context = {}
#     return render(request, "registration/register.html", context)


# def logout(request):
#     logout(request)
#     return redirect("main/home.html")
