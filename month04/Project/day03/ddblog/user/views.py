from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views import View
from .models import UserProfile
import hashlib
import jwt
import time


class UserView(View):
    # 这里面的名字必须与请求方法一样。
    # 在as_view()里针对不同请求方式，在试图类中去查找对应的类的方法（封装在django里面）找到调用，没找到直接报异常
    # 异常码405 请求的方法不存在
    def get(self, request):
        return HttpResponse('--user get--')

    def post(self, request):
        # 1. 获取前段给后端的json串
        json_str = request.body
        # 2. 把json串反序列化为对象
        json_obj = json.loads(json_str)
        # 3. 从对象【字典】中获取数据
        username = json_obj['username']
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        # 4. 数据检查
        # 4.1 检查数据的用户名是否可以用
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10100, 'error': '用户名已注册'}
            return JsonResponse(result)
        # 4.2 两次密码是否一致
        if password_1 != password_2:
            result = {'code': 10101, 'error': '两次密码不一致'}
            return JsonResponse(result)
        # 4.3 添加密码哈希值
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_h = md5.hexdigest()

        # 4.4 数据入库
        # 在高并发情况下仍然需要try
        try:
            user = UserProfile.objects.create(username=username, password=password_h, email=email, phone=phone,
                                              nickname=username)
        except:
            result = {'code': 10102, 'error': '用户名已注册'}  # 虽然返回的错误都是用户名已注册，但是，产生错误的时机不一样。所以错误代码不一样
            return JsonResponse(result)
        # 6. 如何记住登录状态
        #   以前的云笔记项目中，我们使用session保存登录状态
        #   博客项目中使用刚刚学习的token
        token = make_token(username)
        token = token.decode()
        # 不decode的话，字节串验证的时候会出现错误
        # 把字节串转换成字符串
        return JsonResponse({'code': 200, 'username': username, 'data': {'token': token}})


def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    # 生成token
    return jwt.encode(payload, key, algorithm='HS256')

# 官方jwt encode会把其变成token（字节串）