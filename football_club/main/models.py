from django.db import models

# Create your models here.


class PostNews(models.Model):
    title = models.CharField(max_length=70, help_text="Введите название поста")
    text = models.TextField(help_text="Содержание Статьи")
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

