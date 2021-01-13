from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def index_view(request):
    return render(request, 'base.html')


def sports_view(request):
    return render(request, 'sports.html')


def news_view(request):
    return render(request, "news.html")


def pagen_view(request, num):
    # num = num
    # return render(request, "pagen.html", locals())
    reverse('pagen_url', args=[200])
    return HttpResponse(f'this is No.{num}')


def test_static(request):
    return render(request, 'test_static.html')

def index2_view(request):
    return render(request,'index.html')
