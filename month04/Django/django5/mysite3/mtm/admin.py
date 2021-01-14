from django.contrib import admin
from .models import *


# Register your models here.

class AuthorManager(admin.ModelAdmin):
    list_display = ['name']


class BookManager(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Author, AuthorManager)
admin.site.register(Book, BookManager)
