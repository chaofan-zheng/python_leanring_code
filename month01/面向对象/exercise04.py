"""
    练习:
        创建敌人类
        创建实例变量并保证数据在有效范围内
            姓名、血量、攻击力
                  0-100  1 – 30
"""


class Enemy:
    def __init__(self, name, blood, attack):
        self.name = name
        self.blood = blood
        self.attack = attack

    @property
    def blood(self):
        return self.__blood

    @property
    def attack(self):
        return self.__attack

    @blood.setter
    def blood(self, value):
        if 0 <= value <= 100:
            self.__blood = value
        else:
            raise Exception("血量必须在0～100之间")

    @attack.setter
    def attack(self, value):
        if 1 <= value <= 30:
            self.__attack = value
        else:
            raise Exception("攻击力必须在1～30之间")


enemy_dog = Enemy("狗", 50, 10)
enemy_dog.blood = 10000
print(enemy_dog.__dict__)