"""
僵尸进程演示
* join 在阻塞等待子进程，子进程退出时会清理僵尸
* 每次start前会自动清理已经产生的僵尸
"""
from multiprocessing import Process
from time import sleep
import os
from signal import *

# 忽略子进程退出行为
signal(SIGCHLD,SIG_IGN)

# 进程执行函数
def fun():
    print("开始运行一个进程:",os.getpid())
    sleep(2)
    print("终于完成事情结束喽")

# 实例化进程对象
p1 = Process(target=fun)
p1.start()
sleep(3)

p2 = Process(target=fun)
p2.start()

p.join()



