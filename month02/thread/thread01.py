"""
线程基础示例
"""
from threading import Thread
from time import sleep
import os

a = 1


# 线程执行函数
def music():
    global a
    print("a=", a)  # a= 1
    a = 10000
    for i in range(3):
        sleep(2)
        print(os.getpid(), "播放：画画的baby")


t = Thread(target=music)

t.start()

for i in range(4):
    sleep(1)
    print(os.getpid(), "奔驰的小野马和带刺的玫瑰")

t.join()
print("a=", a)  # a= 10000,多个线程共用进程的资源
