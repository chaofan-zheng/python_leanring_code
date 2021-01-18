from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .models import Book


def all_books(request):
    all_book = Book.objects.all()
    return render(request, 'bookstore/all_books.html', locals())


def add_book(request):
    if request.method == "GET":
        return render(request, 'bookstore/add_book.html')
    elif request.method == "POST":
        # 1. 获取客户端提交的表单数据
        title = request.POST['title']
        pub = request.POST['pub']
        price = request.POST['price']
        market_price = request.POST['market_price']
        # print(title, pub, price, market_price)
        # return HttpResponse('添加数据成功')

        # 2. 使用这些数据，在后端的数据库中创建一条记录
        Book.objects.create(title=title, pub=pub, price=price, market_price=market_price)
        return HttpResponseRedirect('all_books')


def update_book(request, book_num):
    dict01 = {}
    try:
        book = Book.objects.get(id=book_num)
    except:
        return HttpResponse('图书编号错误！')
    if request.method == "GET":
        dict01['book'] = book
        return render(request, 'bookstore/update_book.html', dict01)
    elif request.method == "POST":
        book.title = request.POST['title']
        book.pub = request.POST['pub']
        book.price = request.POST['price']
        book.market_price = request.POST['market_price']
        book.save()
        # 使用重定向
        return HttpResponseRedirect('all_books')


def delete_book(request):
    book_id = request.GET.get('book_id')
    try:
        book = Book.objects.get(id=book_id)
    except:
        return HttpResponse('图书编号错误')
    book.delete()

    return HttpResponseRedirect('all_books')


def test(request):
    books = Book.objects.filter(Q(price__gt=50) & Q(market_price__gte=90))
    return render(request, 'bookstore/test.html', locals())
