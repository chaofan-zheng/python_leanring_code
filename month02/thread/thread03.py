"""
自定义线程类
"""
from threading import Thread


class MyThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("播放：画画的baby")


my_thread = MyThread()
my_thread.start()
my_thread.join()