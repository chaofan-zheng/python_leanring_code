"""
以面向对象的思想,描述下列情景.
   (1)需求：小明使用手机打电话
   (2)小明一次请多个保洁打扫卫生
      效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
   (3)张无忌教赵敏九阳神功
   赵敏教张无忌玉女心经
   张无忌工作挣了5000元
   赵敏工作挣了10000元
"""


class Person:
    def __init__(self, name):
        self.name = name

    def use_phone(self, phone):
        phone.call()


class Phone:
    def call(self):
        print("打电话")


xiaoming = Person("小明")
phone = Phone()
xiaoming.use_phone(phone)

# 第二小题
print()


class People:
    def __init__(self, name):
        self.name = name

    # def ask_for_housekeeping(self, cleaner_list):
    #     for cleaner_name in cleaner_list:
    #         cleaner = Cleaner(cleaner_name)
    #         cleaner.clean()
    # 上面的方法可以，但是每一次调用，调用的人就需要构建列表。就很麻烦

    def ask_for_housekeeping(self, *args):
        for cleaner_name in args:
            cleaner = Cleaner(cleaner_name)
            cleaner.clean()
    # 这个方法每次调用的时候传递名字就行了

class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean(self):
        print(f"{self.name}正在工作")


xiaoming = People("小明")
cleaner_list = ["小阿giao", "小药水", "老马"]


# xiaoming.ask_for_housekeeping(cleaner_list)
xiaoming.ask_for_housekeeping("小阿giao", "小药水", "老马")

"""
    张无忌教赵敏九阳神功
    赵敏教张无忌玉女心经
    张无忌工作挣了5000元
    赵敏工作挣了10000元
"""
print()


class Character:
    def __init__(self, name):
        self.name = name

    def teach(self, student, course):
        print(f"{self.name}教{student}{course}")

    def go_to_work(self, salary):
        print(f"{self.name}工作挣了{salary}元")


zwj = Character("张无忌")
zm = Character("赵敏")
zwj.teach("赵敏", "九阳神功")
zm.teach("张无忌", "玉女心经")
zwj.go_to_work(5000)
zm.go_to_work(10000)
