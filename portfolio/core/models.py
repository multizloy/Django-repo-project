from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to="static/images/")
    next_image = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
            # Получаем URL следующей фотографии
            self.next_image = self.image.url
            self.save()