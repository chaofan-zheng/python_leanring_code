from django.contrib import admin

# Register your models here.
from .models import Book


# 创建一个模型管理器类，用于管理Book模型类 (必须继承于admin.ModelAdmin)
class BookManage(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price', 'market_price']
    list_display_links = ['id', 'title', 'pub', 'price', 'market_price']
    list_filter = ['pub']
    search_fields = ['title', 'pub']


admin.site.register(Book, BookManage)
