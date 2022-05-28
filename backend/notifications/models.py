from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from handles.models import Handle
from kindles.models import DirectKindle, SeekingKindle

User = get_user_model()


class Actor(models.Model):
    handle = models.OneToOneField(
        Handle, null=True, blank=True, on_delete=models.CASCADE
    )
    direct_kindle = models.OneToOneField(
        DirectKindle, null=True, blank=True, on_delete=models.CASCADE
    )
    seeking_kindle = models.OneToOneField(
        SeekingKindle, null=True, blank=True, on_delete=models.CASCADE
    )

    @property
    def actor(self):
        if self.handle:
            return self.handle
        elif self.direct_kindle:
            return self.direct_handle
        elif self.seeking_kindle:
            return self.seeking_kindle

    def __str__(self):
        return f"{self.actor}"


class Notification(models.Model):
    sender = models.ForeignKey(
        Actor, on_delete=models.PROTECT, related_name="notification_sender"
    )
    recipient = models.ForeignKey(
        Actor, on_delete=models.PROTECT, related_name="notification_recipient"
    )
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=512, blank=True)
    unread = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.sender.actor} to {self.recipient.actor}"
