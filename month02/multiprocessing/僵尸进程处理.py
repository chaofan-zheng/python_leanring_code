"""
僵尸进程演示
"""
from multiprocessing import Process
from time import sleep
import os
from signal import *

signal(SIGCHLD, SIG_IGN)  # 断绝父子关系


def fun():
    print("开始第一个任务", os.getpid())
    sleep(1)
    print("任务结束了")


# 每一次start之前都会清理之前已经出现的僵尸
p1 = Process(target=fun)
p1.start()
sleep(3)
p2 = Process(target=fun)
p2.start()

# 同时start多个子进程，不回收，会产生多个僵尸进程
p1 = Process(target=fun)
p2 = Process(target=fun)
p1.start()
p2.start()

# Linux操作系统下产生僵尸进程的原因 Windows 下不会产生
# 在子进程死亡的时候，操作系统会发送一个signal去告知父进程，若父进程不处理（没有join）就会产生僵尸进程
# 所以也可以用signal去断绝父子关系，操作系统就不会告知父进程，而是自己回收。
# 孤儿进程是操作系统会自己回收
