from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django_email_verification import send_email
from django.http import HttpResponseRedirect
from django.urls import reverse

User = get_user_model()

from .forms import Login_Form, User_Update_Form, UserCreateForm

# UserRegistrationForm


# Register new user
def register_user(request):
    if request.user.is_authenticated:
        return redirect("shop:products")
    if request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            user_email = form.cleaned_data.get("email")
            user_username = form.cleaned_data.get("username")
            user_password = form.cleaned_data.get("password1")

            # Create new user
            user = User.objects.create_user(
                username=user_username, email=user_email, password=user_password
            )
            # Make user inactive until they click link to token in email
            user.is_active = False
            send_email(user)

            return redirect("/account/email-verification-sent/")
            # return redirect("shop:products")
            # return HttpResponseRedirect(reverse("account:login"))
    else:
        form = UserCreateForm()
    return render(request, "account/register.html", {"form": form})


def login_user(request):
    form = Login_Form()

    if request.user.is_authenticated:
        return redirect("shop:products")

    if request.method == "POST":
        form = Login_Form(request.POST)

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("account:dashboard")
        else:
            messages.info(request, "Username or Password is incorrect")
            return redirect("account:login")
    context = {"form": form}
    return render(request, "account/login.html", context)


def logout_user(request):
    logout(request)
    return redirect("shop:products")


@login_required(login_url="account:login")
def dashboard(request):
    return render(request, "account/dashboard/dashboard.html")


@login_required(login_url="account:login")
def profile_management(request):
    if request.method == "POST":
        form = User_Update_Form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated")
            return redirect("account:profile-management")
        else:
            messages.error(request, "Please correct the error below")
    else:
        form = User_Update_Form(instance=request.user)
    context = {"form": form}

    return render(request, "account/dashboard/profile-management.html", context)


@login_required(login_url="account:login")
def profile_delete(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        user.delete()
        logout(request)
        return redirect("shop:products")
    return render(request, "account/dashboard/account-delete.html")
