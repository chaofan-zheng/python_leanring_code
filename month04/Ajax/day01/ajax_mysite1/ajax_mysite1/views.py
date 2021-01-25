import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def test_xhr(request):
    return render(request, 'test_xhr.html')


def test_xhr_get(request):
    return render(request, 'test_xhr_get.html')


def test_xhr_get_server(request):
    return HttpResponse('This is Ajax Data!')


def test_jq_get(request):
    return render(request, 'test_jq_get.html')


def test_json(request):
    return render(request, 'test_json.html')


def my_test(request):
    json_arr = [
        {
            'name': 'tedu',
            'age': 18,
        },
        {
            'name': 'Aiden',
            'age': 20,
        },
    ]
    jsonStr = json.dumps(json_arr)
    return HttpResponse(jsonStr)


def make_js(request):
    dict1 = {
        'name': 'tedu',
        'age': 18,
    }
    return JsonResponse(dict1)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        print(uname, pwd)
        return HttpResponse(f'注册成功！{uname}')


def test_cross(request):
    return render(request, 'cross.html')


def cross_server(request):
    func = request.GET.get('callback')
    return HttpResponse(func+"('我跨域来了')")