import os
import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

import csv

from django.views.decorators.csrf import csrf_exempt

# from . import settings
# 在django函数中使用当时的配置文件时，django要求我们使用django内置的settings文件
from django.conf import settings

from test_upload.models import Content


@cache_page(30)
def test_cache(request):
    t1 = time.time()
    # 模拟耗时的操作（可以是复杂的查询，也可以是复杂的计算）
    time.sleep(3)
    print('---------- view in ------------')  # 打印的话说明走了视图，有缓存的话不会走视图
    return HttpResponse(f'time is {t1}')


def test_mw(request):
    print('my view in')
    return HttpResponse('my middleware view!')


def test(request):
    return HttpResponse('This is the page of test')


def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    if request.method == 'POST':
        username = request.POST['username']
        return HttpResponse(f'username is {username}')


def test_page(request):
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    paginator = Paginator(list1, 2)
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, 'test_page.html', locals())


def test_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    # 创建一个csv的写入器
    writer = csv.writer(response)
    writer.writerow(['图书编号', '图书名称'])
    # 准备数据
    all_books = [
        {'id': 1, 'title': 'python'},
        {'id': 2, 'title': 'c++'},
        {'id': 3, 'title': 'java'},
    ]
    # 写入数据
    for book in all_books:
        writer.writerow([book['id'], book['title']])
    return response


@csrf_exempt
def test_upload(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == 'POST':

        # 第一种方式
        # # 如果没有文件的话会报错
        # file_upload = request.FILES['myfile']
        # print('上传的文件名是：', file_upload.name)
        # filename = os.path.join(settings.MEDIA_ROOT, file_upload.name)
        # with open(filename, 'wb') as f:
        #     data = file_upload.file.read()
        #     f.write(data)
        #
        # return HttpResponse('接收文件:'+filename+'成功，文件描述：'+request.POST['title'])

        # 第二种方式
        title = request.POST['title']
        file_upload = request.FILES['myfile']
        Content.objects.create(desc=title,myfile = file_upload)
        return HttpResponse('------upload is ok-------')
