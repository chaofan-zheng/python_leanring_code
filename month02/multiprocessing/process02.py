"""
包含参数的进程函数
"""
from time import sleep
from multiprocessing import Process


def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % name)
        print("I'm working")


p = Process(target=worker,
            args=(2,),
            kwargs={"name":"Aiden"})
p.start()
p.join()
