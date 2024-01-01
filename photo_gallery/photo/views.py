from django.shortcuts import render
from .models import Photo
from django.http import HttpResponse

# Create your views here.


from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Photo
from django.http import HttpResponse


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
    # return render(request, "photo/gallery.html", context)
    return HttpResponse(render_to_string('photo/gallery.html', context))

