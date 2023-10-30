from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PostNews(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=None,
        null=None,
    )
    title = models.CharField(max_length=70, help_text="Введите название поста")
    text = models.TextField(help_text="Содержание Статьи")
    time_created = models.DateTimeField(
        auto_now_add=True, db_comment="Date and time when the article was published"
    )
    time_modified = models.DateTimeField(
        auto_now=True,
        db_comment="Date and time when the article was modified",
        blank=None,
        null=None,
    )

    def __str__(self):
        return self.title
