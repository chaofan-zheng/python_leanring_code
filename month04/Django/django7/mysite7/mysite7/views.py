import time

from django.http import HttpResponse
from django.views.decorators.cache import cache_page


@cache_page(30)
def test_cache(request):
    t1 = time.time()
    # 模拟耗时的操作（可以是复杂的查询，也可以是复杂的计算）
    time.sleep(3)
    print('---------- view in ------------') # 打印的话说明走了视图，有缓存的话不会走视图
    return HttpResponse(f'time is {t1}')
