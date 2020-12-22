"""
继承练习1
冰淇淋小店
冰淇淋小店是一个特殊的餐馆。编写一个名为IceCreamStand的类，继承之前的Restaurant类。创造flavors的属性，用于存储一个有各种口味冰淇淋的列表。
编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。
"""


class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"餐厅的名称为{self.name}，餐厅的类别的{self.type}")

    def open_restaurant(self):
        print("餐厅正在营业")

    def print_number_served(self):
        print(f"有{self.number_served}人在{self.name}就餐过")

    def set_number_served(self, new_number):
        if new_number > 0:
            self.number_served = new_number
        else:
            print("就餐人数不能小于0")


class IceCreamStand(Restaurant):
    def __init__(self, name, type, *args):
        super().__init__(name, type)
        self.flavor = list(args)

    def print_all_iceream(self):
        print(f"{self.name}的口味有{self.flavor}")


Haagen_Dazs = IceCreamStand("Hagen Dazs", "ice cream", "vanilla", "regular", "honey nut")
Haagen_Dazs.print_all_iceream()

list01 = [1,2,3]
list01.index(1)