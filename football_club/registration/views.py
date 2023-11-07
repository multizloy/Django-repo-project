from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import generic
from .models import UserProfile
from django.contrib.auth.models import User

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


# def my_dashboard(request):
#     if request.user.is_authenticated:
#         me = request.user.id
#         f_name = request.user.first_name
#         l_name = request.user.last_name
#         email = request.user.email
#         role = request.user.is_user
#         nickname = request.user

#         context = {
#             "f_name": f_name,
#             "l_name": l_name,
#             "email": email,
#             "role": role,
#             "nickname": nickname,
#         }
#         return render(request, "registration/dashboard.html", context)


class Dashboard(generic.CreateView):
    template_name = "registration/dashboard.html"
    form_class = User_Profile_Update_Form
    context_object_name = "profiles"
    success_url = reverse_lazy("registration:dashboard")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        me = self.request.user
        # profile = UserProfile.objects.filter(
        #     username=me, email=me, first_name=me, last_name=me
        # )
        return UserProfile.objects.filter(
            username=me, email=me, first_name=me, last_name=me
        )
