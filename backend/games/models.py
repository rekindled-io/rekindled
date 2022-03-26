import os
from django.db import models


def rename_and_set_upload_path(instance, filename):
    _, ext = os.path.splitext(filename)

    return f"cover/{instance.slug}{ext}"


class Game(models.Model):
    name = models.CharField(null=False, unique=True, max_length=128)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(default="image.jpg", upload_to=rename_and_set_upload_path)
    platforms = models.ManyToManyField(
        "Platform", through="GameAndPlatform", related_name="+"
    )

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=32, unique=True)
    games = models.ManyToManyField(Game, through="GameAndPlatform", related_name="+")

    def __str__(self):
        return self.name


class GameAndPlatform(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.game} ({self.platform})"
