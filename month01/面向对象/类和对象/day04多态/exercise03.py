"""
说出图形管理器中的设计原则的体现
"""
import math

# 开闭原则：能增加三角形等具体图形，但是不用修改图形管理器
class GraphicsControl:
    def __init__(self):
        self.__all_graphic = []  # 进行封装，对外面无用，就藏起来。

    def append_list_graphics(self, graphic):
        if isinstance(graphic, Graphics):  # 这样就不会报错

            self.__all_graphic.append(graphic)

    def calculate_all_area(self):
        for graphic in self.__all_graphic:
            graphic.calculate_area()


class Graphics:
    # 图形管理器与各种图形是组合关系
    # 图形类与圆形/矩形类是继承关系
    # 依赖倒置 依赖Graphic来管理子类，也是继承复用的体现
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass


# 上面是架构师做的事情
# 下面是程序员做的事情，程序员做的时候，不能够破坏下面的结构


# 单一职责，圆形类只负责计算圆形类的面积
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
        # 建议用super().父类方法
        # 图形类隔离了图形管理器和图形之间的关系，迪米特原则


use = GraphicsControl()
use.append_list_graphics(Circle("圆", 4))
use.append_list_graphics(Rectangle("长方形", 4, 5))
use.append_list_graphics("三角")
use.calculate_all_area()
