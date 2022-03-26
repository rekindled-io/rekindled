from django.contrib import admin
from django.db.models import Count

from .models import Game, GameAndPlatform, Platform


class GameAndPlatformInline(admin.TabularInline):
    model = GameAndPlatform
    extra = 1


@admin.register(Game)
class GamesAdmin(admin.ModelAdmin):
    inlines = [GameAndPlatformInline]


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass


@admin.register(GameAndPlatform)
class GameAndPlatformAdmin(admin.ModelAdmin):
    pass
