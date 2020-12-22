"""
位置实参+关键字实参
"""


def time_calculator(hour=0, minute=0, second=0):
    result = hour * 3600 + minute * 60 + second
    return result


print(time_calculator(minute=5, second=10))
print(time_calculator())
print(time_calculator(9, 9, 6))
print(time_calculator(1, second=8))

list01 = [1, 2, 3, 4, 5, 6, 7]
str01 = "孙悟空"


def func02(*args):
    print(args)


func02()
func02(1)
func02(1, 2, 3)
func02(*list01)
func02(*str01)
print(*list01)


def func03(*args, p1, p2):
    print(args)
    print(p1)
    print(p2)


func03(p1=10, p2=20)
# func03(1, 2, 3, p2=3)  # func03() missing 1 required keyword-only argument: 'p1'
print()


def func04(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


dict01 = {"p2": 20, "p3": 30, "p1": 10}
func04(**dict01)
func04(*dict01)  # 一个星，就把键值进去了（按照顺序对应）


def func05(**kwargs):  # 将多个形参，转化成一个字典
    print(kwargs)


func05(p1=1, p2=2)
