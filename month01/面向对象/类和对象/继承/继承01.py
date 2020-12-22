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

    def print_odometer(self):
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

    def fill_gas_tank(self):
        print("your gas tank has been filled.")


# 继承，创建子类

class ElectricCar(Car):
    def __init__(self, make, model, year, remaining_battery):
        """
        继承父类Car的实例变量和方法
        :param make:
        :param model:
        :param year:
        """
        super().__init__(make, model, year)  # 所有的父类实例变量、方法都会继承
        self.battery_size = 70    # 默认子类实例变量
        self.remaining_battery = remaining_battery  # 子类自定义实例变量

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

    def fill_gas_tank(self):       # 重写父类方法
        print("Electric car doesn't have gas tank!")


my_tesla = ElectricCar('tesla', 'ModelX', 2020, 90)
print(my_tesla.get_describe_name())  # 调用父类的方法
my_tesla.update_odometer(13000)  # 调用父类的方法
my_tesla.print_odometer()  # 调用父类的方法
my_tesla.describe_battery() # 调用子类方法
my_tesla.read_remaining_battery() # 调用子类方法
my_tesla.fill_gas_tank()  # 调用经过重写的父类方法
