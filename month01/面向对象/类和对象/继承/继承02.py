"""
# 将类的一个对象，作为一个大类里面的一个属性
- 使用代码模拟时，会发现自己给类添加的细节越来越多，实例变量和方法都越来越长，这种情况下，就需要将类的一部分作为一个独立的类提取出来。
- 下面把针对汽车电瓶的属性和方法都提取出来，放到另一个Battery的类中，并将一个Battery对象用作ElectricCar类的一个属性

"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_describe_name(self):
        """
        打印车子的基本信息
        :return: long_name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:  # 定义一个类来管理电池
    def __init__(self, remaining_battery):
        self.battery_size = 70
        self.remaining_battery = remaining_battery

    def describe_battery(self):
        """
        子类方法：打印电池容量
        :return: none
        """
        print(f"This car has a {self.battery_size} -kWh battery")

    def read_remaining_battery(self):
        """
        子类方法，打印剩余电量
        :return: none
        """
        print(f"This car has {self.remaining_battery} % battery left")

    def get_range(self):  # 新增
        if 80 < self.battery_size < 100:
            print("这车的剩余电量还能开大约500km")
        elif 50 < self.battery_size < 80:
            print("这车的剩余电量大约还能开300km")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)  # 先将父类的属性继承过来
        self.battery = Battery(remaining_battery=90)  # 初始化特有属性，将一个类作为实例变量，后续调用的时候要找到这个特殊的实例变量，再去找方法


my_tesla = ElectricCar("Tesla", "modelX", "2020")
print(my_tesla.get_describe_name())  # 父类的函数也可以调用
my_tesla.battery.describe_battery()  ###
my_tesla.battery.read_remaining_battery()  ###
my_tesla.battery.battery_size = 55
my_tesla.battery.get_range()  ##新增
