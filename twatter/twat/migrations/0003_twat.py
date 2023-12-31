# Generated by Django 5.0 on 2023-12-28 17:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twat", "0002_profile_date_modified"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Twat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(max_length=140)),
                ("date_posted", models.DateTimeField(auto_now_add=True)),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="twats",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
