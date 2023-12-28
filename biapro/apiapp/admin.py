# admin.py

from django.contrib import admin
from .models import Book

# Register your Book model
admin.site.register(Book)
