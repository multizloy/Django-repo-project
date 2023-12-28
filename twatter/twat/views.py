from .models import Profile, Twat
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        twats = Twat.objects.all().order_by("-date_posted")
    context = {"twats": twats}
    return render(request, "twat/index.html", context)


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        context = {"profiles": profiles}
        return render(request, "twat/profile_list.html", context)
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect("twat:index")


def profile(request, pk):
    if request.user.is_authenticated:
        twats = Twat.objects.all().filter(user_id=pk).order_by("-date_posted")
        profile = Profile.objects.get(user_id=pk)
        # POst form logic
        if request.method == "POST":
            # Get current user profile
            current_user_profile = request.user.profile
            # Get data form
            action = request.POST["follow-btn"]
            # decide to follow or unfollow
            if action == "follow":
                current_user_profile.follows.add(profile)
                messages.success(request, "You have followed this user.")
            else:
                # unfollow
                current_user_profile.follows.remove(profile)
                messages.success(request, "You have unfollowed this user.")
            # save the profile
            current_user_profile.save()

        context = {"profile": profile, "twats": twats}
        return render(request, "twat/profile.html", context)
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect("twat:index")
