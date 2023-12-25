from random import randint
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from registration.models import User
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.
from django.template.defaultfilters import slugify as django_slugify

# Slugify (Cyrillic)
alphabet = {
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ё": "yo",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "j",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "ts",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "ы": "i",
    "э": "e",
    "ю": "yu",
    "я": "ya",
}


def slugify(s):
    return django_slugify("".join(alphabet.get(w, w) for w in s.lower()))


class PostNews(models.Model):
    title = models.CharField(max_length=70, help_text="Введите название поста")
    text = models.TextField(help_text="Содержание Статьи")
    slug = models.CharField(max_length=1000, null=True, blank=True)

    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        editable=False,  # Запретить изменения чтобы убрать из ручного редактирования
        db_index=True,
    )

    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # cохряняем названия в юрл строке, первая строчка для уникальности статей с одинаковыми заголовками
    def save(self, *args, **kwargs):
        if PostNews.objects.filter(title=self.title).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.title) + "/" + extra
        else:
            self.slug = slugify(self.title)
        super(PostNews, self).save(*args, **kwargs)
