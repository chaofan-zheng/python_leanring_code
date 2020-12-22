"""
设计思想
    分而治之
    变则疏之

类与类行为不同
"""

# 需求：老张开车去东北
# 分析：
#     老张/老李/老孙      驾驶
#     车       行驶
#     东北不应该做成类，因为没有什么行为和数据，
#     但是当东北有名字，坐标，美食等其他信息的时候，需要进行封装。
"""
建立类与类之间的交互
    （1）直接创建对象调用。老张每次去东北都会有一辆新车
    （2）构造函数创建对象。老张每次开自己的车去东北；缺点在于人与车绑死了。
    （3）通过参数传递对象。老张每次用交通工具去东北
"""


# 方法一：直接在类里创建对象进行调用，特点在于每一次调用方法，都会创建新的对象。
class Person:
    def __init__(self, name):
        self.name = name

    def drive(self):
        car = Car()
        print(f"{self.name}驾驶")
        car.run()


class Car:
    def run(self):
        print("行驶")


lz = Person("老张")
lz.drive()


# 方法二：构造函数创建对象,特点在于，Person的对象与车相互关联，一个Person对象有一个专有的车，每次都是开车去东北

class Person:
    def __init__(self, name):
        self.name = name
        self.__car = Car()

    def drive(self):
        print(f"{self.name}驾驶")
        self.__car.run()


class Car:
    def run(self):
        print("行驶")


lz = Person("老张")
lz.drive()

# 方法三，通过参数传递,这样每次就可以自定义传递的参数，每次可以开不同的车，也可以开飞机

class Person:
    def __init__(self, name):
        self.name = name

    def drive(self,car):
        print(f"{self.name}驾驶")
        car.run()


class Car:
    def run(self):
        print("行驶")


lz = Person("老张")
lz.drive(Car())