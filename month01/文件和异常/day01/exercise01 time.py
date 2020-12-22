"""
    根据年月日，计算星期
"""
import time


def get_week_by_day(year, month, day):
    str_time = "%d-%d-%d" % (year, month, day)
    time_tuple = time.strptime(str_time, "%Y-%m-%d")
    return int(time_tuple[6]) + 1


print(get_week_by_day(2020, 11, 19))
