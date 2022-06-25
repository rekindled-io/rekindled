from django.contrib import admin

from .models import Actor, Notification


@admin.register(Notification)
class Notification(admin.ModelAdmin):
    readonly_fields = ["timestamp"]


@admin.register(Actor)
class Actor(admin.ModelAdmin):
    pass
