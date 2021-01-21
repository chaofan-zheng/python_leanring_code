from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import redis

# Create your views here.

r = redis.Redis(password='417355570')


def user_detail(request, uid):
    cache_key = f'user_{uid}'
    # 西安判断是否有缓存，有缓存就用缓存，没有就读取mysql里面的数据（读的时候因为用的是get，所以容易报错，要get一下），
    # 然后写入缓存，为下一次访问提供方便
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        # 类型是字典，键和值都是二进制字节串
        # 类型转化
        new_data = {k.decode(): v.decode() for k, v in data.items()}
        result = f"redis: username is {new_data['username']}, age is {new_data['age']}, city in {new_data['city']}"
        return HttpResponse(result)
    else:
        try:
            user = User.objects.get(id=uid)
        except:
            return HttpResponse('用户id错误')
        # 然后写入缓存，为下一次访问提供方便
        r.hset(cache_key, 'username', user.username)
        r.hset(cache_key, 'age', user.age)
        r.hset(cache_key, 'city', user.city)
        r.expire(cache_key, 120)  # 设置有效期30s
        # 返回响应
        result = f'mysql:username is {user.username}, age is {user.age}, city in {user.city}'
        return HttpResponse(result)


def user_update(request, uid):
    # 使用查询字符串获取年龄
    age = request.GET.get('age', 18)
    city = request.GET.get('city', 'beijing')
    # 一查二改三保存
    try:
        user = User.objects.get(id = uid)
    except:
        return HttpResponse('用户id错误')
    user.age = age
    user.city = city
    user.save()
    # 清除缓存
    # 如果不清除的话会等到过期了以后才会显示出更改
    cache_key = f'user_{uid}'
    r.delete(cache_key)
    return HttpResponse('更新用户数据成功')