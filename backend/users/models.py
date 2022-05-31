from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    email_confirmed = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email"]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=32, blank=True)
    discord_name = models.CharField(max_length=32, blank=True, null=True)
    discord_account_number = models.IntegerField(blank=True, null=True)
    discord_id = models.CharField(max_length=32, blank=True, null=True)
    steam_id = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s profile"
