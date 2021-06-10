from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Budget


# Run this function every time a User is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # if User was created
        Budget.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_budget(sender, instance, **kwargs):
    instance.budget.save()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

