"""
创建多个线程
线程函数传参
"""
from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    print("含有参数的线程来喽")
    sleep(sec)
    print("%s线程执行完啦"%name)

# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,
               args=(2,),
               kwargs={'name':"T-%d"%i})
    jobs.append(t)
    t.start()

# 循环回收
for i in jobs:
    i.join()