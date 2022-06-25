from django.contrib import admin
from django.db.models import Count

from .models import Game, GameAndPlatform, Platform


class GameAndPlatformInline(admin.TabularInline):
    model = GameAndPlatform
    extra = 1


@admin.register(Game)
class GamesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [GameAndPlatformInline]
    ordering = ['name']


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    ordering = ['name']


@admin.register(GameAndPlatform)
class GameAndPlatformAdmin(admin.ModelAdmin):
    ordering = ['game__name']
