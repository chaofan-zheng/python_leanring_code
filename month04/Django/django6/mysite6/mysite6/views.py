from django.http import HttpResponse


def set_cookies(request):
    resp = HttpResponse('设置cookies成功')
    resp.set_cookie('uname', 'aid2010', 60)
    return resp


def get_cookies(request):
    uname = request.COOKIES.get('uname', 'default value')
    res = f'uname is {uname}'
    return HttpResponse(res)


def delete_cookies(request):
    resp = HttpResponse('删除cookies成功')
    resp.delete_cookie('uname')
    return resp


def set_session(request):
    request.session['uname'] = 'Aiden'
    return HttpResponse('set session is ok')


def get_session(request):
    uname01 = request.session['uname']
    uname02 = request.session.get('uname', 'there is no uname in session')
    res = f'uname01 = {uname01}, uname02 = {uname02}'
    return HttpResponse(res)


def delete_session(request):
    if 'uname' in request.session:
        del request.session['uname']
    return HttpResponse('you have deleted this session')
