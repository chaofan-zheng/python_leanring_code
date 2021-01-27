import jwt
from django.conf import settings
from django.http import JsonResponse

from user.models import UserProfile


def login_check(func):
    def wrap(request, *arg, **kwargs):
        # 在请求中获取前端提交过来的token
        # 前端在每次发送请求前，都将token放进去一起发送（Authorization）
        # 先认证有没有登录
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
            result = {'code': 403, 'error': 'please log in ! '}
            return JsonResponse(result)
        # token的校验
        # try:
        #     # 在decode方法中，首先会验签，签名是否有效
        #     # 然后验签通过后，从payload获取有效期，判断token是否在有效期内
        #     payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithm='HS256')
        # except:
        #     result = {'code': 403, 'error': '请先登录!'}
        #     return JsonResponse(result)
        payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithm='HS256')
        # 从结果中获取私有声明
        username = payload['username']
        # 根据用户名名称获取用户对象
        user = UserProfile.objects.get(username=username)
        # 将用户对象作为request的附加属性
        request.myuser = user

        # myuser名是任意的，自定义的
        return func(request, *arg, **kwargs)

    return wrap
