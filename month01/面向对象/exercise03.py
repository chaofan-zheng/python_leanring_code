"""
    对象计数器
        统计一个类型创建过多少对象
        要求:通过类变量实现
             画出内存图
"""


# 一个类
class Wife:
    count = 0

    @classmethod
    def count_object(cls):
        print("有%d个老婆" % Wife.count)

    def __init__(self, name):
        self.name = name
        Wife.count += 1


# 五个对象
wife01 = Wife("A")
wife02 = Wife("B")
wife03 = Wife("C")
wife04 = Wife("d")
wife05 = Wife("e")
Wife.count_object()


