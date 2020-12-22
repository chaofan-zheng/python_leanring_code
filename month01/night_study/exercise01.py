"""
    重写range函数，range(5)生成5,4,3,2,1,0
"""


class MyRangeIterator:
    def __init__(self, begin_num, end_num=0):
        self.end_num = end_num
        self.begin_num = begin_num
        self.num = self.begin_num + 1

    def __next__(self):
        self.num -= 1
        if self.num < self.end_num:
            raise StopIteration
        return self.num


class MyRange:
    def __init__(self, begin_num):
        self.begin_num = begin_num

    def __iter__(self):
        return MyRangeIterator(self.begin_num)


for i in MyRange(5):
    print(i)


# 重新做一个能够将不可迭代对象变成可迭代对象
class MyClassIterator:
    def __init__(self, object):
        self.list = object
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index > len(self.list) - 1:
            raise StopIteration
        return self.list[self.index].parameter01, self.list[self.index].parameter02, self.list[self.index].parameter03


class MyClass:
    def __init__(self, parameter01=0, parameter02=0, parameter03=0):
        self.parameter03 = parameter03
        self.parameter02 = parameter02
        self.parameter01 = parameter01
        self.list = []

    def __iter__(self):
        return MyClassIterator(self.list)

    def add_my_class(self, parameter01, parameter02, parameter03):
        self.list.append(MyClass(parameter01, parameter02, parameter03))


my_class = MyClass()
my_class.add_my_class(1, 1, 1)
my_class.add_my_class(2, 2, 2)
my_class.add_my_class(3, 3, 3)

for item in my_class:
    print(item)
