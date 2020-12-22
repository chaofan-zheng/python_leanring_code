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


my_new_car = Car("audi", "a4L", 2019)
print(my_new_car.get_describe_name())
my_new_car.print_odometer()

# 有三种方法可以修改实例变量
# 方法1：直接修改实例变量的值
my_new_car = Car("audi", "a4L", 2019)
print(my_new_car.get_describe_name())
my_new_car.odometer_reading = 23
my_new_car.print_odometer()

# 方法2：通过方法修改属性的值（见16行）,也可以添加一些逻辑验证
my_new_car = Car("audi", "a4L", 2019)
print(my_new_car.get_describe_name())
my_new_car.odometer_reading = 23
my_new_car.update_odometer(11)  # 执行不了
my_new_car.print_odometer()
my_new_car.update_odometer(46)  # 可以执行
my_new_car.print_odometer()