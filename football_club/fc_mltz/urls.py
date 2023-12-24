from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("registration/", include("registration.urls")),
    path("", include("main.urls")),
    path("store/", include("store.urls")),
    path("cart/", include("cart.urls")),
    re_path(r"^imagefit/", include("imagefit.urls")),
    path("unicorn/", include("django_unicorn.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
