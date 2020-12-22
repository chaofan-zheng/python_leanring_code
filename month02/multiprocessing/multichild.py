"""
创建多个子进程
"""
from multiprocessing import Process
from time import sleep
import os, sys


def th1():
    sleep(1)
    print("吃饭")
    print(os.getppid(), "--", os.getpid())


def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(), "--", os.getpid())


def th3():
    sleep(3)
    print("打豆豆")
    print(os.getppid(), "--", os.getpid())


jobs = []
for th in [th1, th2, th3]:
    p = Process(target=th)
    jobs.append(p)  # 存储进程对象
    p.start()

[i.join() for i in jobs]   # 用这种方法来统一回收
# 这个回收不能够写在循环里，不然会等待第一个子进程th1运行完成才会进行第二个子进程，就不会同时进行
