"""
进程池示例
"""
from multiprocessing import Pool
from time import *
from random import random


# 事件需在创建进程池之前就全部写好，因为进程池在创建的同时就会开始进程
def worker(msg, sec):
    begin_time = ctime()
    sleep(sec)  # 每次处理订单的时间
    print("begin:", begin_time, "end", ctime(), "---", msg)


# 创建进程池
pool = Pool()

# 将事件加入到进程池执行等待队列
for i in range(1, 21):
    msg = "订单-%d" % i
    pool.apply_async(worker, args=(msg, 1))

# 当父进程结束的时候会自动关闭进程池

pool.close()
pool.join()
