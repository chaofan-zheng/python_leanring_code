"""
：为 sum_data,增加打印函数执行时间的功能.
函数执行时间公式： 执行后时间 - 执行前时间
"""
import time


def calculate_running_time(func):
    def wrapper(*args, **kwargs):
        begin_time = time.time()
        result = func(*args, **kwargs) # 不能在这里return把函数给断了
        end_time = time.time()
        result_time = end_time - begin_time
        return result,result_time

    return wrapper


@calculate_running_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(10))
print(sum_data(1000000))
