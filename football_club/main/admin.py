from django.contrib import admin
from .models import PostNews
from django.contrib import admin

# Register your models here.

admin.site.register(PostNews)


class PostNewsAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = self.user

        super(PostNewsAdmin, self).save_model(
            request=request, obj=obj, form=form, change=change
        )
