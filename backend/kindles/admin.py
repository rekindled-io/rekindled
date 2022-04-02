from django.contrib import admin

from .models import DirectKindle, SeekingKindle


@admin.register(DirectKindle)
class DirectKindle(admin.ModelAdmin):
    list_display = ["__str__", "source_user"]

    search_fields = ["source_user__username"]


@admin.register(SeekingKindle)
class SeekingKindle(admin.ModelAdmin):
    list_display = ["__str__", "source_user"]

    search_fields = ["source_user__username"]
