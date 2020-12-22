"""
练习：
    创建父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
    创建子类对象并画出内存图。
"""


class Car:
    def __init__(self, brand="", speed=0):
        self.brand = brand
        self.speed = speed


class ElectricCar(Car):
    def __init__(self, brand, speed, battery_capacity=0, charging_efficiency=0):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charging_efficiency = charging_efficiency


my_Audi_r8 = Car("Audi", 210)
my_Tesla = ElectricCar("Tesla", 120, 510, 40)
