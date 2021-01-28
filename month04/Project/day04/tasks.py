from celery import Celery
import time

# 1 初始化celery，指定broker，创建celery对象
app = Celery('aid2010',
             broker='redis://@127.0.0.1:6379/1',
             backend='redis://@127.0.0.1:6379/2'
             )


# 2 创建任务函数
@app.task
def task_test():
    time.sleep(3)
    print('task is running')
