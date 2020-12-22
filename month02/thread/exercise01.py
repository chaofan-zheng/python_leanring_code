"""
现在有500张车票，记为T1--T500
共有10个窗口同时卖票 w1 -- w10
编写一个程序模拟卖票过程
卖出一张则打印 w1 --- T200
卖出后隔0.1 s 才能卖出下一张
"""
from threading import Thread
from time import sleep
from random import random

tick_pool = []
for i in range(1, 501):
    tick_pool.append(f"T{i}")


def sell_ticket(port_name):
    # while tick_pool:
    #     tick_name = tick_pool[0]
    #     del tick_pool[0]
    #     # sleep(random() * 3)
    #     print(f"{port_name}---{tick_name}")
    #     sleep(0.1)

# 线程共享资源的争夺问题
    while tick_pool:
        print(f"{port_name}---{tick_pool[0]}")   # 容易重复,也会有几率超出范围（例如最后只剩两张票了，同时有三个进程进来，删除就会越界）
        del tick_pool[0]
        sleep(0.1)

# while tick_pool:
#     sleep(0.1)   # 容易超出范围
#     print(f"{port_name}---{tick_pool[0]}")
#     del tick_pool[0]

jobs = []
for i in range(11):
    t = Thread(target=sell_ticket,
               args=(f"w{i}",),
               daemon=True
               )
    jobs.append(t)
    t.start()

[job.join() for job in jobs]


