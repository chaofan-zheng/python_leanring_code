"""
    创建狗类
        数据：品种、爱称、年龄、体重
        行为：吃、叫
    实例化两个对象并调用其方法
    画出内存图
    体会:不同狗对象,具有不同的数据.
"""


class Dog:
    def __init__(self, breed, pet_name, age, weight):
        self.breed = breed
        self.pet_name = pet_name
        self.age = age
        self.weight = weight

    def eat(self):
        print(self.breed + "eat")

    def call(self):
        print(self.breed + "wangwangwang")


hashiqi = Dog("哈士奇", "二哈", 5, 10)
bianmu = Dog("边牧", "清华三好生", 3, 8)

hashiqi.eat()
hashiqi.call()
bianmu.eat()
bianmu.call()

# 练习
d01 = Dog("拉布拉多", "米咻", 5, 70)
list_dogs = [
    d01,
    Dog("拉布拉多", "黑米", 4, 60),
    Dog("黑背", "哮天犬", 4, 30),
    Dog("藏獒", "小黑", 4, 80),
]


# 练习1:创建函数,在狗列表中查找品种是"黑背"的狗对象(如果有多个也查找第一个)

def find_by_breed(breed):
    for dog in list_dogs:
        if dog.breed == breed:
            return dog


# 练习2:创建函数,在狗列表中查找所有体重大于10的狗对象

def find_weight_bigger_than_10():
    list_weight_bigger_than_10 = []
    for dog in list_dogs:
        if dog.weight > 10:
            list_weight_bigger_than_10.append(dog)
    return list_weight_bigger_than_10


result = find_by_breed("黑背")
print(result.pet_name)
# result = find_by_breed("哈士奇")
# print(result.pet_name)

print(find_weight_bigger_than_10())  # 打印所有狗对象的地址
# 所以我们只能打印对象里面的一个实例变量
result_bigger_than_10 = find_weight_bigger_than_10()
for item in result_bigger_than_10:
    print(item.breed, item.pet_name, item.weight)
