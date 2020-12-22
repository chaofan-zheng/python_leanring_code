"""
属性各种写法
"""

"""# 读写属性
# 适用性：有一个实例变量，但是需要对读取和写入进行限制
# 快捷键：props + 回车"""


class MyClass:
    def __init__(self, data=0):
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


m01 = MyClass(10)
print(m01.data)

"""# 只读属性
# 适用性： 有一个私有变量，不想让别人改，只想让别人拿。只想提供读取功能，不想提供类外修改
# 快捷键 prop + 回车"""


class MyClass:
    def __init__(self, data=0):
        self.__data = data

    @property
    def data(self):
        return self.__data


m01 = MyClass(10)
print(m01.data)
# m01.data =20 #'MyClass' object has no attribute '_MyClass__data'

"""
只写属性
适用性：只需要修改实例变量，不需要读取
快捷键：无
"""


class MyClass:
    def __init__(self, data=0):
        self.data = data

    data = property()

    @data.setter
    def data(self, value):
        self.__data = value


m01 = MyClass(10)
# print(m01.data)  # AttributeError: unreadable attribute
m01.data = 20
