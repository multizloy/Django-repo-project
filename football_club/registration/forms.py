from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.models import AbstractUser, User


# User = AbstractUser


class MyUserCreationForm(UserCreationForm):
    email_address = forms.EmailField(required=True)

    first_name = forms.CharField(required=False, help_text="Not required.")
    last_name = forms.CharField(required=False, help_text="Not required.")

    class Meta:
        model = User
        fields = (
            "username",
            "email_address",
            "password1",
            "password2",
            "first_name",
            "last_name",
        )


class User_Profile_Update_Form(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )
