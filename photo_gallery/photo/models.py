from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="static/images/photo")

    def __str__(self):
        return self.title


