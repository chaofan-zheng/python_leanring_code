from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
import json
from user.models import UserProfile
import hashlib
from user.views import make_token


class TokenView(View):
    def post(self, request):
        # 1. 获取前端传递的json串
        json_str = request.body
        # 2. 将json串序列化为对象
        json_obj = json.loads(json_str)
        # 3. 获取用户名和密码
        username = json_obj['username']
        password = json_obj['password']
        # 4. 校验用户名和密码
        try:
            user = UserProfile.objects.get(username=username)
        except:
            result = {'code': 10200, 'error': '用户名或密码错误！'}
            return JsonResponse(result)
        # 计算密码的hash
        md5 = hashlib.md5()
        md5.update(password.encode())
        password_h = md5.hexdigest()
        # 与数据库中的密码的hash值比对
        if password_h != user.password:
            result = {'code': 10201, 'error': '用户名或密码错误！'}
            return JsonResponse(result)
        # 5 校验成功后，签发token
        token = make_token(username)
        # token = token.decode()
        return JsonResponse({'code': 200, 'username': username,
                             'data': {'token': token}})
