from django.contrib import admin

from main.forms import Post_News_Form
from .models import PostNews
from django.contrib import admin

# Register your models here.


# class PostNewsAdmin(admin.ModelAdmin):
#     form = Post_News_Form

#     def get_form(self, request, *args, **kwargs):
#         form = super(PostNewsAdmin, self).get_form(request, *args, **kwargs)
#         form.current_user = request.user
#         return form


class PostNewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["author"]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user

        super(PostNewsAdmin, self).save_model(
            request=request, obj=obj, form=form, change=change
        )


admin.site.register(PostNews, PostNewsAdmin)
