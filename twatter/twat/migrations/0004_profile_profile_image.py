# Generated by Django 5.0 on 2023-12-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("twat", "0003_twat"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/profile-image/"
            ),
        ),
    ]
