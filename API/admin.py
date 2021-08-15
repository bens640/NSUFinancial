from django.contrib import admin
from .models import Document,  Category

# Register model for admin site access
admin.site.register(Document)
admin.site.register(Category)


