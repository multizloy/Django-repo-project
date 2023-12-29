from django import forms
from .models import Profile, Twat
from django.contrib.auth.models import User


class Twat_Form(forms.ModelForm):
    content = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={"placeholder": "Enter Your Twat!", "class": "form-control"}
        ),
        required=True,
        label="",
    )

    class Meta:
        model = Twat
        exclude = (
            "user",
            "likes",
        )


class Profile_Form(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile picture", required=False)

    class Meta:
        model = Profile
        fields = ("profile_image",)


class Profile_Update_Form(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "User Name"}
        ),
    )
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]


# class Change_Password_Form(forms.Form):
#     current_password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={"class": "form-control", "placeholder": "Current password"}
#         )
#     )
#     new_password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={"class": "form-control", "placeholder": "New password"}
#         )
#     )
#     confirm_new_password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={"class": "form-control", "placeholder": "Repeat new password"}
#         )
#     )
