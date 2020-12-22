"""
一个用于表示汽车的类
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 默认实例变量

    def get_describe_name(self):
        """
        打印车子的基本信息
        :return: long_name
        """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """
        打印车子公里数
        :return: none
        """
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, new_mile):
        """
        在外部调用方法，经过逻辑验证之后，设置新的英里数
        :param new_mile: 新的英里数
        :return: none
        """
        if new_mile >= self.odometer_reading:
            self.odometer_reading = new_mile  # 通过方法，修改实例变量
        else:
            print("you can not roll back an odometer!")

    def increment_odometer(self, miles):
        """
        将里程表读书增加指定的量
        :param miles: 需要增加的公里数
        :return: none
        """
        self.odometer_reading += miles


class Battery():
    """一次模拟电动车电瓶的简单尝试"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size} -kWh battery")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        print(f"This car can go approximately {range} miles on a full charge")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
