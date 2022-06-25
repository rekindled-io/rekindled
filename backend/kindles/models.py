from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from games.models import GameAndPlatform
from handles.models import Handle

User = get_user_model()


class BaseKindle(models.Model):
    source_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related"
    )
    source_handle = models.ForeignKey(
        Handle, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related"
    )
    message = models.TextField(max_length=512, blank=True)

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "source_user",
                    "source_handle",
                    "target_handle",
                ],
                name="%(class)s_unique_kindle",
            )
        ]

    def __str__(self):
        return f"#{self.id} - {self.source_user.username} to {self.source_handle}"


class SeekingKindle(BaseKindle):
    target_handle = models.CharField(max_length=64, blank=False, null=False)
    game_and_platform = models.ForeignKey(
        GameAndPlatform, blank=False, null=False, on_delete=models.CASCADE
    )
    subscribe = models.BooleanField(default=True)


class DirectKindle(BaseKindle):
    target_handle = models.ForeignKey(
        Handle, blank=False, null=False, on_delete=models.CASCADE
    )
