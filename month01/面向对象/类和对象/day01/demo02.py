class Wife:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property  # 保障数据在有效范围之内
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 22 <= value <= 30:
            self.__age = value
        else:
            raise Exception("我不要")


w01 = Wife("ABCD", 25)
print(w01.age)
print(w01.__dict__)