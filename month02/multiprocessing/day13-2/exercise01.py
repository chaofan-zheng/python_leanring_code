"""
编写程序求 100000以内质数之和
编写一个装饰器求 这个过程的时间
使用4个进程做同样的事情，求时间
使用10个进程做同样的事情，求时间
"""
import time
from multiprocessing import Process

#　装饰器求函数运行时间
def timeis(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        print("函数执行时间:",end_time - start_time)
        return  res
    return  wrapper

# 自定义进程类
class Prime(Process):
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
def process_4():
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(i,i+25000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

# 函数执行时间1: 13.316346883773804
# 函数执行时间4: 9.136988162994385
# 函数执行时间10: 7.718727111816406
# 函数执行时间20: 7.239355564117432
process_4()


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
# def process_one():
#     prime = []
#     for i in range(100001):
#         if is_prime(i):
#             prime.append(i)
#     print(sum(prime))
#
# # 函数执行时间: 13.316346883773804
# process_one()
