"""
创建多个子进程
"""
from multiprocessing import Process
from time import sleep
import os,sys

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),"--",os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(),"--",os.getpid())

def th3():
    sleep(4)
    sys.exit("不打豆豆啦") # 该进程结束
    print("打豆豆")
    print(os.getppid(),"--",os.getpid())

# 循环创建进程
jobs = []
for th in [th1,th2,th3]:
    p = Process(target=th)
    jobs.append(p) # 存储进程对象
    p.start()

# 统一的回收进程
[i.join() for i in jobs]





