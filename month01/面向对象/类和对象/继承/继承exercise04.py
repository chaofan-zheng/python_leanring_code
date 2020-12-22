"""
练习04 电瓶升级
在之前的电动车版本中，给Battery类添加一个名为upgrade_battery()的方法。这个方法检查电瓶容量，如果它不是85，就将它设置为85，
创建一瓶电瓶容量为默认值的电动汽车，调用放大get_range()，然后对电瓶进行升级，并且再次调用get_range(),然后对电瓶进行升级，并再次调用get_range().
会看到续航里程增加了
"""


class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year


class ElectricCar(Car):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        self.battery = Battery()


class Battery:
    def __init__(self):
        self.battery_capacity = 70

    def upgrade_battery(self):
        if self.battery_capacity != 85:
            self.battery_capacity = 85

    def get_range(self):
        if 80 < self.battery_capacity:
            print("这辆车还能够跑600km")
        elif 50 < self.battery_capacity <= 80:
            print("这辆车还能够跑350km")
        else:
            print("这辆车快没电了")


my_tesla = ElectricCar("Tesla", "modelX", "2020")
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
