from django.contrib import admin
from .models import User, UserProfile, Footballer, Trainer, Store_Manager

# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Footballer)
admin.site.register(Trainer)
admin.site.register(Store_Manager)
