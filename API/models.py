from django.contrib.auth.models import User
from django.db import models


class Document(models.Model):
    # Enumeration for type field to limit user entry
    DOC_TYPE = (
        ('LINK', 'link'),
        ('PDF', 'pdf')
    )
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=DOC_TYPE)
    link = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.title} : {self.type}'


class Budget(models.Model):
    date_created = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, default=0, max_digits=10)

    def __str__(self):
        return f'{self.user.username}\'s Budget '


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_base = models.BooleanField(default=False)
    parent_cat = models.ForeignKey(to='self', null=True, blank=True, on_delete=models.CASCADE)
    is_income = models.BooleanField(default=False)

    def __str__(self):
        if self.parent_cat is None:
            return f'Category: {self.name}'
        else:
            return f'Sub-Category: {self.name}, Parent Category: {self.parent_cat}'


class Transaction(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date_created = models.DateField(auto_now_add=True)
    transaction_date = models.DateField(auto_now_add=False)
