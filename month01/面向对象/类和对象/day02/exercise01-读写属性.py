"""
练习2:创建技能类，并保护数据在有效范围内
数据：技能名称,冷却时间,  攻击力度,  消耗法力
                        0 -- 120  0 -- 200  100 -- 100
"""


class Skills:
    def __init__(self, name="", cd=0, attack=0, consumption=0):
        self.cd = cd
        self.attack = attack
        self.consumption = consumption
        self.name = name

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        if 0 <= value <= 100:
            self.__cd = value
        else:
            raise Exception("cd要在1～120s")

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        if 0 <= value <= 200:
            self.__attck = value
        else:
            raise Exception("攻击力要在0～200之间")

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, value):
        if value == 100:
            self.__consumption = value
        else:
            raise Exception("消耗法力为100")

giao = Skills("giao",2,200,100)
