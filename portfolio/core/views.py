from django.shortcuts import render
from .models import Photo

# Create your views here.


def index(request):
    photos = Photo.objects.all()
    context = {"photos": photos}
    return render(request, "core/index.html", context)
