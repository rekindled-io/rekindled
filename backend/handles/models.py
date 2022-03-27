from django.contrib.auth import get_user_model
from django.db import models

from games.models import GameAndPlatform

User = get_user_model()


class Handle(models.Model):
    class RegionChoices(models.TextChoices):
        AFRICA = "AF", "Africa"
        ANTARCTICA = "AN", "Antarctica"
        ASIA = "AS", "Asia"
        EUROPE = "EU", "Europe"
        NORTHAMERICA = "NA", "North America"
        OCEANIA = "OC", "Oceania"
        SOUTHAMIERCA = "SA", "South America"
        WORLDWIDE = "WW", "Worldwide"

    name = models.CharField(max_length=64, blank=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="handles",
    )
    game_and_platform = models.ForeignKey(
        GameAndPlatform, null=False, blank=False, on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    start_period = models.DateField(blank=True, null=True)
    end_period = models.DateField(blank=True, null=True)
    region = models.CharField(
        max_length=2, choices=RegionChoices.choices, default=RegionChoices.WORLDWIDE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name", "game_and_platform"], name="unique-handle"
            ),
        ]

    def __str__(self):
        return f"#{self.pk} {self.name}"
