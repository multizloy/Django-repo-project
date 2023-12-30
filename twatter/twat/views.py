from .models import Profile, Twat
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import Twat_Form, Profile_Form, Profile_Update_Form, Change_Password_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from registration.forms import Register_Form


# Create your views here.
def index(request):
    # Handles the main index view for authenticated users.
    # Allows posting new twats via a form.
    # Displays paginated list of twats.
    # For unauthenticated users, just displays the twat list.
    if request.user.is_authenticated:
        form = Twat_Form(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                twat = form.save(commit=False)
                twat.user = request.user
                twat.save()
                messages.success(request, "Twat posted successfully")
                return redirect("twat:index")
            else:
                messages.error(request, "Twat not posted")

        twats = Twat.objects.all().order_by("-date_posted")
        context = {"twats": twats, "form": form}
        return render(request, "twat/index.html", context)
    else:
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


def profile_edit(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        current_profile = Profile.objects.get(user_id=request.user.id)
        # передает функцию для смены Юзернейма, имени, фамилии, почты
        user_form = Profile_Update_Form(
            request.POST or None, request.FILES or None, instance=current_user
        )
        # передает функцию для смены картинки профиля
        profile_form = Profile_Form(
            request.POST or None, request.FILES or None, instance=current_profile
        )

        if request.method == "POST":
            if user_form.is_valid() and profile_form.is_valid()():
                user_form.save()
                profile_form.save()

                messages.success(request, "Profile updated successfully")
                return redirect("twat:profile", pk=request.user.id)
            else:
                messages.error(request, "Profile not updated")
        context = {
            "user_form": user_form,
            "profile_form": profile_form,
        }
        return render(request, "twat/profile_edit.html", context)
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect("twat:index")


def twat_like(request, pk):
    if request.user.is_authenticated:
        twat = get_object_or_404(Twat, id=pk)
        if twat.likes.filter(id=request.user.id):
            messages.success(
                request,
                "You disliked" + " " + str(twat.content) + " by" + " @" + str(twat.user),
            )
            twat.likes.remove(request.user)
        else:
            messages.success(
                request,
                "You liked" + " " + str(twat.content) + " by" + " @" + str(twat.user),
            )
            twat.likes.add(request.user)

        return redirect(request.META.get("HTTP_REFERER"))

    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect("twat:index")


def twat_share(request, pk):
    if request.user.is_authenticated:
        twat = get_object_or_404(Twat, id=pk)
        if twat:
            return render(request, "twat/twat_share.html", {"twat": twat})
        else:
            messages.success(request, "This twat doesn`t exist.")
            return redirect("twat:index")
