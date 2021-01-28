import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from .models import UserProfile
import json
import hashlib
import jwt
import time
from django.conf import settings
# from ddblog import settings as my_settings
from tools.login_dec import login_check
from django.core.cache import cache
from tools.sms import YunTongXin
from .task import send_sms

class UserView(View):
    # 处理 v1/users的 GET 请求
    def get(self, request, username=None):
        if username:
            # 返回指定用户的信息
            try:
                user = UserProfile.objects.get(username=username)
            except:
                result = {'code': 10104, 'error': '用户名称错误！'}
                return JsonResponse(result)

            if request.GET.keys():
                # 获取指定信息
                data = {}
                for k in request.GET.keys():
                    if k == 'password':
                        continue
                    if hasattr(user, k):
                        data[k] = getattr(user, k)
                result = {'code': 200, 'username': username,
                          'data': data}

            else:
                # 返回指定用户的全量信息
                result = {'code': 200, 'username': username,
                          'data': {'info': user.info, 'sign': user.sign,
                                   'nickname': user.nickname,
                                   'avatar': str(user.avatar)}}
            return JsonResponse(result)

        else:
            return HttpResponse('-返回所有用户信息-')

    # 处理 v1/users的 POST 请求
    def post(self, request):
        # 1.获取前端给后端的json串
        json_str = request.body
        # 2.把json串反序列化为对象
        json_obj = json.loads(json_str)
        # 3.从对象【字典】中获取数据
        username = json_obj['username']
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']
        # 从前端中获取用户输入的验证码
        sms_num = json_obj['sms_num']
        # 从redis中读取的验证码
        cache_key = f"sms_{phone}"
        code = cache.get(cache_key)
        # 验证验证码
        if not code:
            result = {'code': 10110, "error": "验证码已失效"}
            return JsonResponse(result)
        if int(sms_num) != code:
            result = {'code': 10111, 'error': '验证码不一致'}
            return JsonResponse(result)
        # 4 数据检查
        # 4.1 检查注册的用户名是否可以使用
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            result = {'code': 10100, 'error': '用户名已注册'}
            return JsonResponse(result)
        # 4.2 两次密码是否一致
        if password_1 != password_2:
            result = {'code': 10101, 'error': '两次密码不一致'}
            return JsonResponse(result)
        # 4.3 添加密码的hash值
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_h = md5.hexdigest()

        # 5 插入数据【仍然需要try】
        try:
            user = UserProfile.objects.create(username=username,
                                              password=password_h,
                                              email=email,
                                              phone=phone,
                                              nickname=username)
        except:
            result = {'code': 10102, 'error': '用户名已注册'}
            return JsonResponse(result)

        # 6 如何记住登录状态
        # 以前的云笔记项目中，我们使用的session保存登录状态
        # 博客项目中使用刚刚学习的token
        token = make_token(username)
        # print(token)
        # 为什么要decode？将生成的字节串转换为字符串
        # token = token.decode()
        # print(token)
        return JsonResponse({'code': 200, 'username': username,
                             'data': {'token': token}})

    # 处理 v1/users的 PUT请求
    @method_decorator(login_check)
    def put(self, request, username):  # 用不用是一回事，你可以写了不用，但是不写会在path转换器上报错
        # 登录检查不能够直接用login_check的装饰器
        # 借助于method_decorator
        # 1. 获取前段传递的json串
        json_str = request.body
        # 2. 反序列化为对象
        json_obj = json.loads(json_str)
        # 3. 获取要修改的用户
        user = request.myuser
        # myuser里面放的是登录的用户对象（mysql）
        #         # 根据用户名称获取用户对象
        #         user = UserProfile.objects.get(username=username)
        #         # 将用户对象作为request的附加属性
        #         request.myuser = user
        # 4. 修改
        user.sign = json_obj['sign']
        user.nickname = json_obj['nickname']
        user.info = json_obj['info']
        # 5. 保存
        user.save()
        # 6. 返回
        result = {'code': 200, 'username': user.username}
        return JsonResponse(result)


def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    # 生成token
    return jwt.encode(payload, key, algorithm='HS256')


@login_check
def user_avatar(request, username):
    if request.method != 'POST':
        result = {'code': 10105, 'error': '只接收post请求'}
        return JsonResponse(result)
    # 从request获取已经登录的用户
    user = request.myuser
    # 修改用户的头像
    user.avatar = request.FILES['avatar']
    # 保存
    user.save()
    # 返回
    result = {'code': 200, 'username': user.username}
    return JsonResponse(result)


def sms_view(request):
    # 获取前端提交的数据
    json_str = request.body
    # 反序列化
    json_obj = json.loads(json_str)
    # 获取手机号码
    phone = json_obj['phone']
    print(phone)
    # 生成随机的验证码发给手机
    code = random.randint(100000, 999999)
    # 将验证码放到redis中
    cache_key = f'sms_{phone}'
    cache.set(cache_key, code, 180)  # 有效时间3分钟，和前端同步
    send_sms.delay(phone,code)

    return JsonResponse({'code': 200})


