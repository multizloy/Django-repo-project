from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

User = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields["email"].label = "Your Email Address"
        self.fields["email"].required = True
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""

    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        if User.objects.filter(email=email).exists() and len(email) > 254:
            raise forms.ValidationError("Email is already in use or too long")

        return email


class Login_Form(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    password = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )


class User_Update_Form(forms.ModelForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(User_Update_Form, self).__init__(*args, **kwargs)

        self.fields["email"].label = "Your Email Address"
        self.fields["email"].required = True

    class Meta:
        model = User
        fields = ["username", "email"]
        exclude = ["password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        if (
            User.objects.filter(email=email).exclude(id=self.instance.id).exists()
            or len(email) > 254
        ):
            raise forms.ValidationError("Email is already in use or too long")

        return email
