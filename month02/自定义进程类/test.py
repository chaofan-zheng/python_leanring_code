"""
自定义进程类
"""
from multiprocessing import Process


# 使用面向对象的思想，创建自己的类
class MyProcess(Process):
    def __init__(self, value, group=None, target=None, name=None, args=(), kwargs={}):
        self.value = value
        super().__init__(group, target, name, args, kwargs)

    # 进行执行内容的入口函数
    def run(self):
        print("重写的run运行了")


def function():
    print("子进程运行了")


my_process = MyProcess(value=3, target=function)  # 这个target并不会运行，因为start会调用run函数，run函数本身会调用target
# 启动进程 进程执行内容从入口函数run引出
my_process.start()
my_process.join()
