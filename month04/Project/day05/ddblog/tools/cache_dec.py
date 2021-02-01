# 写自己的装饰器
from django.core.cache import cache

from tools.login_dec import get_user_by_request


def topic_cache(expire):
    def _topic_cache(func):
        def wrapper(request, *args, **kwargs):
            # 具体的缓存实现
            if 't_id' in request.GET.keys():
                return func(request, *args, **kwargs)
            visitor_name = get_user_by_request(request)
            author_name = kwargs['author_id']
            if visitor_name == author_name:
                # path有三种情况
                # v1/tedu/topics
                # v1/tedu/topics?category=tec
                # v1/tedu/topics?category=no-tec
                cache_key = f'topic_cache_self_{request.get_full_path()}'  # 内置的函数
            else:
                # v1/tedu/topics
                # v1/tedu/topics?category=tec
                # v1/tedu/topics?category=no-tec
                cache_key = f'topic_cache_{request.get_full_path()}'
            print(f'__cache key is {cache_key}__')
            # 缓存思想：有缓存访问缓存，没有缓存，调用视图函数，并存入缓存，返回
            res = cache.get(cache_key)
            if res:
                print('----cache in----')
                return res
            res = func(request, *args, **kwargs)
            cache.set(cache_key, res, expire)
            return res  # 这个为什么要加上

        return wrapper

    return _topic_cache
