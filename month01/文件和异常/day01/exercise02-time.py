"""
    定义函数，根据生日（年月日），计算活了多少天
"""
import time


def calculate_day(year, month, day):
    str_time = "%d-%d-%d" % (year, month, day)
    time_tuple = time.strptime(str_time, "%Y-%m-%d")
    time_mark = time.mktime(time_tuple)
    time_mark_subtracted = time.time() - time_mark
    days = time_mark_subtracted // 86400
    return days


print(calculate_day(1998, 8, 23))