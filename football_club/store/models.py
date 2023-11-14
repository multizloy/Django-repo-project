import django
from django.db import models
from django.core.exceptions import ValidationError
from fc_mltz import settings
from django_resized import ResizedImageField
from registration.models import User

# Create your models here.


# создаем базовые категории вещей в магазине
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# создаем единую модель предметов
class Item(models.Model):
    class Size(models.TextChoices):
        Small = "Маленький"
        Medium = "Средний"
        Large = "Большой"
        Xl = "Огромный"

    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = ResizedImageField(
        size=[300, 200],
        upload_to="static/images",
        blank=True,
        null=True,
    )

    size = models.CharField(choices=Size.choices, default=None)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        null=True,
        on_delete=django.db.models.deletion.PROTECT,
        related_name="Created_by",
        to=settings.AUTH_USER_MODEL,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name

    def image_size_validator_factory(min_w=600, min_h=600, field_name="image"):
        def validator(image):
            if image.width < min_w or image.height < min_h:
                raise ValidationError(
                    {field_name: f"Размер картинки от {min_w}х{min_h} пикселей. "}
                )

        return validator

    def clean(self):
        if self.image:
            image_size_validator_factory()(self.image)
        return super().clean()
