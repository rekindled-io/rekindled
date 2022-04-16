from django.contrib import admin

from .models import Handle


@admin.register(Handle)
class HandleAdmin(admin.ModelAdmin):
    list_display = ["__str__", "game_and_platform", "user"]
    list_filter = [
        "game_and_platform__game",
        "game_and_platform__platform",
        "user",
        "region",
    ]
    search_fields = ["name"]
