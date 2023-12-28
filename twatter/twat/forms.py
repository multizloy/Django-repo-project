from django import forms
from .models import Profile, Twat


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
