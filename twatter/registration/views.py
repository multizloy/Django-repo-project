from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import Register_Form

# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in as " + username)
            return redirect("twat:index")
        else:
            messages.success(request, "Wrong username or password")
            return render(request, "registration/login.html", {})
    return render(request, "registration/login.html", {})


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return render(request, "registration/login.html")


def register_view(request):
    form = Register_Form()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "You have successfully registered as " + username)
            return redirect("twat:index")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registration/register.html", {"form": form})
    return render(request, "registration/register.html", {"form": form})
