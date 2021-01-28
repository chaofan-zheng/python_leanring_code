from django.http import HttpResponse
from django.shortcuts import render
from .task import task_test
import datetime

# Create your views here.
def test_celery(request):
    task_test.delay()  # 执行任务函数
    # 不使用生产者消费者模式
    # task_test()
    now = datetime.datetime.now()
    html = f"return at {now.strftime('%H:%M:%S')}"
    return HttpResponse(html)
