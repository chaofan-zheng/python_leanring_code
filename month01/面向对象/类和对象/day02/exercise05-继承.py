"""
练习：
    创建子类：狗（跑），鸟类（飞）
    创建父类：动物（吃）

"""


class Animals:
    def eat(self):
        print("eat")


class Dogs(Animals):
    def run(self):
        print("跑")


class Bird(Animals):
    def fly(self):
        print("飞")


bird = Bird()
bird.eat()
dog = Dogs()
dog.run()
animal = Animals()

print(isinstance(bird, Bird))  # True
print(isinstance(bird, Animals))  # True # 要确保是实例，父子关系则True
print(isinstance(Bird, Animals))  # False
# print(issubclass(bird, Bird)) # 报错，必须是class
print(issubclass(Animals, Bird))  # False
print(type(bird) == type(Bird))  # False
print(type(bird) == type(bird))  # True
print(type(Bird) == type(Animals))  # True
print(type(bird) == type(dog))  # False
print(type(dog) == Dogs)  # True
print(isinstance(dog,Animals)) # True
print(issubclass(Dogs,Animals)) # True
"""
type 找的是类型
isinstance 找的是是不是实例 父子关系也可以
issubclass 找的是不是子类
"""
