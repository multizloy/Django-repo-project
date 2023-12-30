from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    follows = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers", blank=True
    )
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to="static/images/profile-image/"
    )

    def __str__(self):
        return self.user.username


# Create profile when new user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        # have to user follow himself
        instance.profile.follows.add(instance.profile)


post_save.connect(create_profile, sender=User)


class Twat(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="twats")
    content = models.TextField(max_length=140)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="twat_like", blank=True)

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return (
            f"{self.user}"
            f"({self.date_posted.strftime('%m/%d/%Y, %H:%M:%S')}: "
            f"{self.content})"
        )
