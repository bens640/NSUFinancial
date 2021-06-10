from django.contrib.auth.models import User
from django.db import models


class Loan(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    start_date = models.DateField(null=True)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest = models.DecimalField(max_digits=9, decimal_places=2)
    term = models.IntegerField()

    def __str__(self):
        return self.name


class Document(models.Model):
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

    def __str__(self):
        return f'{self.user.username}\'s Budget '


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_base = models.BooleanField(default=False)
    parent_cat = models.ForeignKey(to='self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if self.parent_cat is None:
            return f'Category: {self.name}'
        else:
            return f'Sub-Category: {self.name}, Parent Category: {self.parent_cat}'


class Transaction(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    transaction_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.id
