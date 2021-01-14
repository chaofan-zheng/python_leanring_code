from django.contrib import admin

# Register your models here.
from .models import *


class PublisherManager(admin.ModelAdmin):
    list_display = ['id', 'name']


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher']


#
admin.site.register(Publisher, PublisherManager)
admin.site.register(Book, BookManager)
