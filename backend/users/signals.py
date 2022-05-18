from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .emails import email_activation

from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def send_confirmation_email(sender, instance, **kwargs):
    user = instance

    if not user.email_confirmed:
        email = email_activation(user)
        email.send()
