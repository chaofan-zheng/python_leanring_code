"""
编写程序求 100000以内质数之和
         编写一个装饰器求 这个过程的时间

         使用4个进程做同样的事情，求时间
         使用10个进程做同样的事情，求时间
"""

import time
from multiprocessing import Process


def get_prime(start, end):
    for num in range(start, end):
        for divider in range(2, num // 2):
            if num % divider == 0:
                break
        else:
            yield num


def sum_result(start, end):
    out = 0
    for num in get_prime(start, end):
        out += num
    return out


def time_calculator(func):
    def wrapper(*args, **kwargs):
        begin_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"运行结果为{result}运行时间为{end_time - begin_time}")
        return result

    return wrapper


def multichild_run(*args):
    process_object = []
    for p_range in args:
        p = Process(target=sum_result, args=p_range)
        process_object.append(p)
        p.start()
    for process in process_object:
        process.join()


@time_calculator
def process01():
    res = sum_result(2, 100000)
    return res


@time_calculator
def process02(*args):
    multichild_run(*args)

# 非阻塞的情况下，不见得进程越多越好
process01()
process02((2, 25000), (25001, 50000), (50001, 75000), (75001, 100000)) # 分到四个内核里面
process02((2, 10000), (10001, 20000), (20001, 30000), (30001, 40000), (40001, 50000), # 分到八个内核里面，有些并发，有些并行
          (50001, 60000), (60001, 70000), (70001, 80000), (80001, 90000), (90000, 100000))
