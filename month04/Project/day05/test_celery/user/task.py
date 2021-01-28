# 做成任务函数的话，是需要导包的
from test_celery.celery import app
import time


@app.task    # 告诉celery这是一个耗时的任务函数
def task_test():
    print('task begin.....')
    time.sleep(10)
    print('task over')

# 使用：celery -A test_celery worker -l info

