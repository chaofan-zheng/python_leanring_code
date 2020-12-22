"""
练习2：创建图形管理器
	1. 记录多种图形（圆形、矩形....）
	2. 提供计算总面积的方法.
    满足：
        开闭原则
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.
"""
import math


class GraphicsControl:
    def __init__(self):
        self.__all_graphic = []   # 进行封装，对外面无用，就藏起来。

    def append_list_graphics(self, graphic):
        if isinstance(graphic,Graphics):    # 这样就不会报错
            
            self.__all_graphic.append(graphic)

    def calculate_all_area(self):
        for graphic in self.__all_graphic:
            graphic.calculate_area()


class Graphics:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass

# 上面是架构师做的事情
# 下面是程序员做的事情，程序员做的时候，不能够破坏下面的结构

class Circle(Graphics):

    def __init__(self, name, r):
        super().__init__(name)
        self.r = r

    def calculate_area(self):
        area = self.r ** 2 * math.pi
        print(f"{self.name}的半径是{self.r},面积是{area}")


class Rectangle(Graphics):

    def __init__(self, name, lenth, width):
        super().__init__(name)
        self.lenth = lenth
        self.width = width

    def calculate_area(self):
        area = self.lenth * self.width
        print(f"{self.name}的长为{self.lenth}，宽是{self.width},面积为{area}")


use = GraphicsControl()
use.append_list_graphics(Circle("圆", 4))
use.append_list_graphics(Rectangle("长方形", 4, 5))
use.append_list_graphics("三角")
use.calculate_all_area()
