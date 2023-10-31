from django.db import models
from django import forms
from .models import PostNews


class Post_News_Form(forms.ModelForm):
    class Meta:
        model = PostNews
        fields = (
            "title",
            "text",
        )
