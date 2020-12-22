"""
函数式编程
    开发过程中，以面向对象为主，以函数式编程思想为辅
    主要的理论支柱：函数可以赋值给变量
"""


def func01():
    print("func01被执行了")


a = func01
a()


# 间接调用
def func02():
    print("func02被执行了")


def func03(func):
    print("func03被执行了")
    func()


# 函数式编程
list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13]


def condition01(item):
    return item > 10


def condition02(item):
    return item < 5


# 通用的
def find(condition):
    for item in list01:
        if condition(item):
            yield item


for item in find(condition01):
    print(item)
