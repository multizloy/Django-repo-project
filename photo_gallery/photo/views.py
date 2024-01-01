from django.shortcuts import render
from .models import Photo


# Create your views here.


def index(request):
    gallery = Photo.objects.all()
    current = request.GET.get("photo")
    if current:
        current = int(current)
    else:
        current = 0
    has_prev = current > 0
    has_next = current < gallery.count() - 1

    context = {
        "gallery": gallery,
        "current": current,
        "has_prev": has_prev,
        "has_next": has_next,
    }
    return render(request, "photo/gallery.html", context)
