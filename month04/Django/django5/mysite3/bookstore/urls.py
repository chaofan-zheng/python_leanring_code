from django.urls import path

from . import views

urlpatterns = [
    # 127.0.01:8000/bookstore/all_books
    path('all_books', views.all_books),
    path('add_book', views.add_book),
    path('update_book<int:book_num>', views.update_book),
    path('delete_book', views.delete_book),
    path('test', views.test),
]
