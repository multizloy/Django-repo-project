from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Twat

# Unregister Group
admin.site.unregister(Group)
admin.site.unregister(User)


# Mix profile info into User info
class Profile_Inline(admin.StackedInline):
    model = Profile
    fields = [
        "follows",
        "profile_image",
    ]


# Extend USer Model
class User_Admin(admin.ModelAdmin):
    model = User
    # Display fields on admin page
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        
    ]
    inlines = [Profile_Inline]


# Register your models here.
admin.site.register(User, User_Admin)
# admin.site.register(Profile)
admin.site.register(Twat)
