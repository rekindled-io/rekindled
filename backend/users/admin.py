from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
