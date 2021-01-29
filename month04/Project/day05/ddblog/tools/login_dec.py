from django.http import JsonResponse
import jwt
from django.conf import settings
from user.models import UserProfile


def login_check(func):
    def wrap(request, *args, **kwargs):
        # 在请求对象中获取前段提交过来的token
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        # 来自于自己
        # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkFpZGVuIiwiZXhwIjoxNjExNzYzOTU3LjkwNzE1OX0.LG67awNavqWW_v_1_yo-hSUuJj6X84QjYINF28znxP0
        # 来自于前端
        # eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkFpZGVuIiwiZXhwIjoxNjExNzYzOTU3LjkwNzE1OX0.LG67awNavqWW_v_1_yo-hSUuJj6X84QjYINF28znxP0
        if not token:
            result = {'code': 403, 'error': 'please log in！'}
            return JsonResponse(result)
        # token的校验
        try:
            # decode方法中，首先会验签，签名是否有效；
            # 验签通过后，从 payload获取有效期，判断token是否在有效期内
            payload = jwt.decode(token,
                                 settings.JWT_TOKEN_KEY,
                                 algorithms=['HS256'])
        except Exception as e:
            print(e)
            result = {'code': 403, 'error': '请登录！'}
            return JsonResponse(result)
        # 从结果中获取私有申明
        username = payload['username']
        # 根据用户名称获取用户对象
        user = UserProfile.objects.get(username=username)
        # 将用户对象作为request的附加属性
        request.myuser = user
        # 调用所修饰的函数
        return func(request, *args, **kwargs)

    return wrap


# 获取文章访问者的信息
def get_user_by_request(request):
    # 没有登录的用户【游客】
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        payload = jwt.decode(token, settings.JWT_TOKEN_KEY, algorithms=['HS256'])
    except:
        return None
    username = payload['username']
    return username