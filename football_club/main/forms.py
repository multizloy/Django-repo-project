from django.db import models
from django import forms
from .models import PostNews
from django.contrib.auth import get_user_model

User = get_user_model()


class Post_News_Form(forms.ModelForm):
    class Meta:
        model = PostNews
        fields = (
            "title",
            "text",
        )

