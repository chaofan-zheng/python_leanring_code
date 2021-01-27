from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.views import View
from .models import UserProfile
from tools.login_dec import login_check
import hashlib
import jwt
import time


class UserView(View):
    # 这里面的名字必须与请求方法一样。
    # 在as_view()里针对不同请求方式，在试图类中去查找对应的类的方法（封装在django里面）找到调用，没找到直接报异常
    # 异常码405 请求的方法不存在
    def get(self, request, username=None):
        if username:
            # 返回指定用户信息
            try:
                user = UserProfile.objects.get(username=username)
            except:
                result = {'code': 10104, 'error': '用户名称有误'}
                return JsonResponse(result)

            if request.GET.keys():
                # 如果在地址栏输入获取一定信息
                # ?sign=1&info=1
                # 获取指定信息
                data = {}
                for k in request.GET.keys():
                    if k == 'password':  # password 想要也不能给
                        continue
                    if hasattr(user, k):
                        data[k] = getattr(user, k)
                result = {'code': 200, 'username': username, 'data': data}

            else:
                # 返回指定用户的全量信息

                # 按格式返回用户信息(在文档里)
                # {‘code’:200,‘username’:’xiaoming’, ‘data’:{‘nickname’:’abc’, ’sign’:’hellow’, ‘avatar’: ’abc.jpg’, ‘info’: ‘hahahahah’}}
                result = {'code': 200, 'username': username,
                          'data': {
                              'info': user.info, 'sign': user.sign, 'nickname': user.nickname,
                              'avatar': str(user.avatar)
                          }}
            return JsonResponse(result)
        else:
            # 如果没有username传进来的话，就如下
            return HttpResponse('--返回所有用户信息--')

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
                                              nickname=username, created_time=time.time())
        except:
            result = {'code': 10102, 'error': '用户名已注册'}  # 虽然返回的错误都是用户名已注册，但是，产生错误的时机不一样。所以错误代码不一样
            return JsonResponse(result)
        # 6. 如何记住登录状态
        #   以前的云笔记项目中，我们使用session保存登录状态
        #   博客项目中使用刚刚学习的token
        token = make_token(username)
        # token = token.decode()
        # 不decode的话，字节串验证的时候会出现错误
        # 把字节串转换成字符串
        return JsonResponse({
            'code': 200, 'username': username,
            'data': {'token': token},
        })


def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    # 生成token
    return jwt.encode(payload, key, algorithm='HS256')


# 官方jwt encode会把其变成token（字节串）,新版会变成字符串

@login_check  # 经过登录认证之后，一定是登录过的用户才能够操作，不然就操作不了
def user_avatar(request, username):
    if request.method != 'POST':
        result = {'code': 10105, 'error': '只能接收post请求'}
        return JsonResponse(result)
    # 获取已经登录的用户
    user = request.myuser
    # 修改用户的头像
    user.avatar = request.FILES['avatar']
    # 保存
    user.save()
    # 返回
    result = {'code': 200, 'username': user.username}
    return JsonResponse(result)
