"""
线程效率检测
"""

import time
from threading import Thread

#　装饰器求函数运行时间
def timeis(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print("函数执行时间:",end_time - start_time)
        return  res
    return  wrapper

# 自定义线程类
class Prime(Thread):
    # 判断一个数是否为质数
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    def __init__(self,begin,end):
        self.begin = begin # 开始数字
        self.end = end # 结尾数字
        super().__init__()

    # 求 从begin--end之间质数之和
    def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if Prime.is_prime(i):
                prime.append(i)
        print(sum(prime))

@timeis
def thread_10():
    jobs = []
    for i in range(1,100001,10000):
        t = Prime(i,i+10000)
        jobs.append(t)
        t.start()
    [i.join() for i in jobs]

# 1 函数执行时间: 13.05928635597229
# 4 函数执行时间: 12.92020559310913
# 10 函数执行时间: 13.000070333480835
thread_10()


# 判断一个数是否为质数
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n // 2 + 1):
#         if n % i == 0:
#             return False
#     return True

#　求10万以内质数之和
# @timeis
# def thread_one():
#     prime = []
#     for i in range(100001):
#         if is_prime(i):
#             prime.append(i)
#     print(sum(prime))

# 函数执行时间: 13.05928635597229
# thread_one()
