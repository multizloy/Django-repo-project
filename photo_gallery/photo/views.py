from django.shortcuts import render
from .models import Photo


# Create your views here.


def index(request):
    gallery = Photo.objects.all()
    current = request.GET.get('photo')
    if current:
        current = int(current)
    context = {
        "gallery": gallery,
        'current': current,

    }
    return render(request, "photo/gallery.html", context)
