from django.db import models
from django.db.models.query import QuerySet
from django.urls import reverse
from django.utils.text import slugify
import random, string


# Generates a random 10 character slug to be used when creating a new Category instance
def rand_slug():
    return "".join(
        random.choice(string.ascii_lowercase + string.digits) for i in range(10)
    )


# Model representing a product category
class Category(models.Model):
    # Category name
    name = models.CharField(max_length=250, db_index=True)

    # Parent category
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    # Category slug
    slug = models.SlugField(max_length=250, unique=True, null=False)

    # Auto-populated created date
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent duplicate slug+parent pairs
        unique_together = ["slug", "parent"]

        # Model verbose names
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    # String representation
    def __str__(self):
        return self.name

    # Override save to auto-generate slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-pickBetter" + self.name)
        super(Category, self).save(*args, **kwargs)


# Model representing a product
class Product(models.Model):
    # Product category
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )

    # Product name
    name = models.CharField(max_length=100)

    # Product brand
    brand = models.CharField(max_length=100)

    # Product description
    description = models.TextField()

    # Product price
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Product slug
    slug = models.SlugField(max_length=48)

    # Product image
    image = models.ImageField(upload_to="products/%Y/%m/%d/")

    # Is in stock
    in_stock = models.BooleanField(default=True)

    # Auto-populated created date
    date_created = models.DateTimeField(auto_now_add=True)

    # Auto-updated modified date
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        # Model verbose names
        verbose_name = "Product"
        verbose_name_plural = "Products"

    # String representation
    def __str__(self):
        return self.name


# Custom manager to filter in-stock products
class Product_Manager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super(Product_Manager, self).get_queryset().filter(in_stock=True)


# Proxy model for in-stock products
class Product_Proxy(Product):
    objects = Product_Manager()

    class Meta:
        proxy = True
