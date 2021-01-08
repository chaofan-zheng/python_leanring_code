from django.http import HttpResponse


# 试图函数
# 参数为请求对象
# 返回值为响应对象


def page_2003(request):
    return HttpResponse('这是编号2003页面')


def page_2004(request):
    return HttpResponse('这是编号2004页面')


def page_index(request):
    # 这里面是html语言
    file = open('test', 'rb')
    f = file.read()
    html = f.decode()
    return HttpResponse(html)
    # return HttpResponse('<h1>不要找小火箭了，我是默认首页index</h1>')


def page_num(request, num):
    return HttpResponse(f'这是编号为{num}的页面')


def page_data(request, data):
    return HttpResponse(f'data:{data}')


def page_path(request, path):
    return HttpResponse(f'path{path}')


def page_op(request, num1, op, num2):
    print(request.method) # 会print在服务台的终端
    print(request.path_info) # "GET /birthday/2/28/1998 HTTP/1.1" 200 25

    if op == 'add':
        return HttpResponse(f'结果为{num1 + num2}')
    elif op == 'sub':
        return HttpResponse(f'结果为{num1 - num2}')
    elif op == 'mul':
        return HttpResponse(f'结果为{num1 * num2}')
    # 测试request对象的使用，从request对象中获取客户端请求的信息

def birthday(request, month, day, year):
    return HttpResponse(f'生日为{year}年{month}月{day}日')
