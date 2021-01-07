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
    file = open('三级联动菜单.html','r')
    f = file.read()
    html=f
    return HttpResponse(html)
    # return HttpResponse('<h1>不要找小火箭了，我是默认首页index</h1>')