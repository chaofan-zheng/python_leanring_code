from django.contrib import admin

# Register your models here.
from .models import Note


class NoteManager(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'updated_time', 'user']


admin.site.register(Note,NoteManager)
