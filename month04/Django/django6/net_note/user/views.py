import hashlib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User


# Create your views here.

def login_view(request):
    if request.method == 'GET':
        if 'uname' in request.session and 'uid' in request.session:
            # 等完成了笔记功能后，直接重定向到笔记列表中
            return HttpResponse('你已经登录了')

        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取数据
        username = request.POST['username']
        password = request.POST['password']
        # 数据检查
        if not username or not password:
            return HttpResponse('用户名和密码不能为空')
        # 查看有无名称为username的用户
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse('用户名或密码错误')
        # 检查密码是否正确
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        if password_h != user.password:
            return HttpResponse('用户名或密码错误')
        request.session['uname'] = username
        request.session['uid'] = user.id

        return HttpResponseRedirect('/note/')


def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        # print(username,password_1,password_2)
        if not username or not password_1:
            return HttpResponse('用户名和密码都不为空')
        if password_1 != password_2:
            return HttpResponse('两次密码不一致！')
        # 名称重复性检查
        old_user = User.objects.filter(username=username)
        if old_user:
            return HttpResponse('用户名已存在')
        # 计算口令的Hash值
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_h = md5.hexdigest()
        # 数据入库
        # 加try的原因是，防止在高并发状态下插入失败
        try:
            User.objects.create(username=username, password=password_h)
        except:
            return HttpResponse('用户名已存在')
        return HttpResponse('注册成功')
        # 注册并登录
        # 查询得到username和userid加到 session里面


def logout_view(request):
    if 'uname' in request.session:
        del request.session['uname']
    if 'uid' in request.session:
        del request.session['uid']
    return HttpResponse('退出登录成功')
