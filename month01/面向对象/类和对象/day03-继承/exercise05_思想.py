"""
练习1：以面向对象思想，描述下列情景：
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图
"""


class Grenade:
    def explode(self, target_injured):
        print("手雷爆炸了")
        target_injured.get_injured()


class TargetInjured:
    def __init__(self, name):
        self.name = name

    def get_injured(self):
        pass


class Player(TargetInjured):

    def get_injured(self):
        print(f"{self.name}受伤了，屏幕碎了")


class Enemy(TargetInjured):

    def get_injured(self):
        print(f"{self.name}受伤了，头顶爆字")


class Duck(TargetInjured):

    def get_injured(self):
        print(f"{self.name}受伤了，变成了全聚德")


player = Player("小阿giao")
duck = Duck("小鸭子")
grenade = Grenade()
grenade.explode(player)
grenade.explode(duck)

