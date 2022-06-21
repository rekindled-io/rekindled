import os
from django.db import models
from functools import partial


def _get_upload_to_path(instance, filename, name):
    _, ext = os.path.splitext(filename)
    return f"{instance.slug}/{name}{ext}"


def rename_and_set_upload_path(name):
    return partial(_get_upload_to_path, name=name)


class Game(models.Model):
    name = models.CharField(null=False, unique=True, max_length=128)
    slug = models.SlugField(null=False, unique=True)
    abbreviation = models.CharField(null=True, unique=True, max_length=8)
    image = models.ImageField(
        default="image.jpg", upload_to=rename_and_set_upload_path(name="image")
    )
    cover = models.ImageField(
        default="cover.jpg", upload_to=rename_and_set_upload_path(name="cover")
    )
    icon = models.ImageField(
        default="icon.jpg", upload_to=rename_and_set_upload_path(name="icon")
    )
    platforms = models.ManyToManyField(
        "Platform", through="GameAndPlatform", related_name="+"
    )

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=32, unique=True)
    abbreviation = models.CharField(null=True, unique=True, max_length=8)
    games = models.ManyToManyField(Game, through="GameAndPlatform", related_name="+")

    def __str__(self):
        return self.name


class GameAndPlatform(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.game} ({self.platform})"
