import decimal

from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .models import Budget, Transaction


# A budget item is created  and saved everytime a user is created
@receiver(post_save, sender=User)
def create_budget(sender, instance, created, **kwargs):
    if created:  # if User was created
        Budget.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_budget(sender, instance, **kwargs):
    instance.budget.save()

# An auth token is generated if a token doesnt already exist
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# When a transaction is saved, the budget balance gets updated
@receiver(post_save, sender=Transaction)
def update_budget_add(sender, instance=None, **kwargs):
    budget = Budget.objects.get(id=instance.budget.id)
    transaction = Transaction.objects.get(id=instance.id)
    budget.balance += transaction.amount
    budget.save()



@receiver(pre_delete, sender=Transaction)
def update_budget_delete(sender, instance=None, **kwargs):
    budget = Budget.objects.get(id=instance.budget.id)
    transaction = Transaction.objects.get(id=instance.id)
    budget.balance -= transaction.amount
    budget.save()
