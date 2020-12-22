"""
练习1 ：
现在有500车票 记为 T1 -- T500
共有10个窗口同时买票 W1--W10

编写一个程序模拟买票过程
卖出一张则打印  w1 -----  T200
卖出后要隔 0.1 秒才能出下一张
卖空为止
"""
from threading import Thread
from time import sleep

# 将车票准备好
ticket = ["T%d" % x for x in range(1,501)]

# 线程函数模拟卖票过程
def sell(w):
    while ticket:
        sleep(0.1)
        print("%s ---- %s"%(w,ticket[0]))
        del ticket[0]


# 创建10个线程
jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=("W%d"%i,))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()