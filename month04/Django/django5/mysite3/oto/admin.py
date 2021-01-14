from django.contrib import admin

# Register your models here.

from .models import *


class AuthorManager(admin.ModelAdmin):
    list_display = ['name','wife']


class WifeManager(admin.ModelAdmin):
    list_display = ['name', 'author']


admin.site.register(Author, AuthorManager)
admin.site.register(Wife, WifeManager)
