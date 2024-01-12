from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect, render

# from . forms import User_Register_Form
from django_email_verification import send_email
from .forms import UserCreateForm

# Create your views here.

User = get_user_model()

def register_user(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user_email = form.cleaned_data.get("email")
            user_username = form.cleaned_data.get("username")
            user_password = form.cleaned_data.get("password1")

            user = User.objects.create_user(
                username=user_username, email=user_email, password=user_password
            )

            user.is_active = False

            send_email(user)
            return redirect("account:login")
    else:
        form = UserCreateForm()
    return render(request, "account/register.html", {"form": form})
