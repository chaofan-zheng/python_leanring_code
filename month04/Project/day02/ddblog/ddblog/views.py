from django.http import HttpResponse
from django.shortcuts import render


def test_cors(request):
    return render(request, 'test_cors.html')


def test_cors_server(request):
    return HttpResponse('this is cors data!')