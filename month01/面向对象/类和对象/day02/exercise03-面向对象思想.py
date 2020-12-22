"""
练习01
用面向对象的方法，描述下列情景
小明请保洁打扫卫生
要求写出三种交互方式
"""

"""
交互方式一
"""
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def hire(self):
#         print("请保洁",end="")
#         cleaner = Cleaner()  # 每次请保洁 都会请一个新的保洁。每次调用hire，都会创建一个新的对象
#         cleaner.clean()
#
#
# class Cleaner:
#     def clean(self):
#         print("打扫卫生")
#
#
# xiaoming = Person("小明")
# xiaoming.hire()

"""交互方式二"""
# class Person:
#     def __init__(self, name):
#         self.name = name
#         实例变量  私有变量
#         self.__cleaner = Cleaner()  # 变成私有变量，锦上添花，因为的小明的保洁不需要去公开这个保洁的信息等
#
#         小明每次去通知自己的保洁
#
#     def hire(self):
#         print("请保洁",end="")
#         self.__cleaner.clean()
#
#
# class Cleaner:
#     def clean(self):
#         print("打扫卫生")
#
#
# xiaoming = Person("小明")
# xiaoming.hire()

"""交互方式三"""


class Person:
    def __init__(self, name):
        self.name = name

    def hire(self, cleaner):
        """
        传入cleaner，在调用的时候要创建对象
        :param cleaner:
        :return:
        """
        print(f"{self.name} 请{cleaner.name}", end=" ")
        cleaner.clean()


class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean(self):
        print("打扫卫生")


xiaoming = Person("小明")
xiaoming.hire(Cleaner("小阿giao"))
