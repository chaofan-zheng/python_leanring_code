"""
定义函数，在列表中查找奇数
定义函数，在列表中查找能被 3或 5 整除的数字
"""
list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def find_odd():
    for item in list01:
        if item % 2 == 1:
            return item


def find_3_5():
    for item in list01:
        if item % 3 == 0 or item % 5 == 0:
            return item


def condition_odd(number):
    return number % 2 == 1


def condtion_3_5(number):
    return number % 3 == 0 or number % 5 == 0


def find(condition_a, condition_b):
    for item in list01:
        if condition_a(item) and condition_b(item):
            yield item


for item in find(condtion_3_5, condition_odd):
    print(item)
