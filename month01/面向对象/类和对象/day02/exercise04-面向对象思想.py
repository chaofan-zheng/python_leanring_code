"""
练习03
以面向对象思想，描述下列情景
玩家攻击敌人，敌人受伤（头顶爆字）
"""

#
# class Player:
#     def __init__(self, name):
#         self.name = name
#
#     def attack(self, enemy):
#         print(f"{self.name} attack, ", end="")
#         enemy.get_injured()
#
#
# class Enemy:
#     def __init__(self, name):
#         self.name = name
#
#     def get_injured(self):
#         print(f"{self.name} get injured")
#
#
# wanjia = Player("I")
# enemy = Enemy("小阿giao")
# wanjia.attack(enemy)

"""
练习04
以面向对象思想，描述下列情景
玩家攻击敌人，敌人受伤（根据玩家攻击力，减少敌人血量）
"""


class Player:
    def __init__(self, name, hp=100, attack=50):
        self.name = name
        self.hp = hp
        self.attack = attack

    def print_infos(self):
        print(f"{self.name} (hp:{self.hp}, attack:{self.attack})")

    def attack_enemy(self, enemy):
        print(f"{self.name} 发动了攻击！")
        enemy.hp -= self.attack


class Enemy:
    def __init__(self, name, hp=100, attack=50):
        self.name = name
        self.hp = hp
        self.attack = attack

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value > 0:
            self.__hp = value
        else:
            print(f"{self.name}死了")
            self.__hp = 0

    def print_infos(self):
        print(f"{self.name} (hp:{self.hp}, attack:{self.attack})")


wanjia02 = Player("我")
enemy02 = Enemy("小阿giao")
print("对局开始！")
wanjia02.print_infos()
enemy02.print_infos()
print()
wanjia02.attack_enemy(enemy02)
wanjia02.print_infos()
enemy02.print_infos()
print()
wanjia02.attack_enemy(enemy02)
wanjia02.print_infos()
enemy02.print_infos()
print()
wanjia02.attack_enemy(enemy02)
wanjia02.print_infos()
enemy02.print_infos()
print()
