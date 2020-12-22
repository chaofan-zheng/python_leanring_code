"""
练习1：创建敌人类，并保护数据在有效范围内
          数据:姓名/ 攻击力/  血量
                     0-100   0-500
"""


class Enemy:
    def __init__(self, name, attack=0, blood=0):
        self.name = name
        self.attack = attack
        self.blood = blood

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if 0 <= value <= 100:
            self.__attack = value
        else:
            raise Exception("攻击力不能超过0～100")

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, value):
        if 0 <= value <= 500:
            self.__blood = value
        else:
            raise Exception("血量不能超过0～500")

    def print_all_info(self):
        print(f"敌人的名字是{self.name}，攻击力为{self.attack}，血量{self.blood}")   # 在调用的时候这里不用隐形变量


monster = Enemy("monster", attack=100, blood=500)
monster.print_all_info()
print(monster.attack)
