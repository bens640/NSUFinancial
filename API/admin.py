from django.contrib import admin
from .models import Loan, Document, Budget, Category, Transaction

# Register your models here.

admin.site.register(Loan)
admin.site.register(Document)
admin.site.register(Budget)
admin.site.register(Category)
admin.site.register(Transaction)
