"""
    老婆类的处理异常
"""
"""
    raise 异常对象
    人为创造异常,是为了快速传递错误消息
"""


class Wife:
    def __init__(self, name="", age=0, salary=0):
        self.salary = salary
        self.name = name
        self.age = age

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if 10000 < value:
            self.__salary = value
        else:
            raise Exception("我不要这个工资", 1002)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 22 <= value <= 30:
            self.__age = value
        else:
            # 人为创造异常对象(传递错误消息)
            raise Exception("我不要这个年纪", 1001)


# 接收异常对象
while True:
    try:
        age = int(input("请输入年龄:"))
        salary = int(input("请输入工资"))
        shuang_er = Wife("双儿", age, salary)
        print(shuang_er.age)
        print(shuang_er.salary)
        break
    except Exception as e:
        print("错误消息是:", e.args)
