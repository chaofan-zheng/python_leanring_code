"""
自定义进程类
"""
from multiprocessing import Process


# 使用面向对象的思想，创建自己的类
class MyProcess(Process):
    def __init__(self, value):
        self.value = value
        super().__init__()

    # 进行执行内容的入口函数
    def run(self):
        print("搞点大事情，想干嘛都行")


my_process = MyProcess(3)
# 启动进程 进程执行内容从入口函数run引出
my_process.start()
my_process.join()
