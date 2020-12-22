"""
    以面向过程的思想，意会以下雷霆战机的架构
"""


class Player:
    def __init__(self, name="", hp=0, attack=0):
        self.name = name
        self.hp = hp
        self.attack = attack

    def moving_byself(self):
        pass

    def being_attacked(self, enemy):
        enemy.enemy_attack()
        self.hp -= enemy.attack
        if self.hp < 0:
            print(f"{self.name}吃面了")
        else:
            print(f"{self.name}受伤了，剩余血量f{self.hp}")

    def attack(self):
        print(f"{self.name}攻击了！")
        print("发射了556子弹")


# class PlayerLevelTwo(Player):
#
#     def __init__(self, hp=0, attack=0):
#         super().__init__(hp, attack)
#
#     def moving(self):
#         super().moving()
#
#     def enemy_attacked(self, enemy):
#         super().being_attacked(enemy)


class Enemy:
    def __init__(self, name=""):
        self.name = name
        self.attack = 0
        self.hp = 0

    def moving(self):
        pass

    def enemy_attack(self):
        print(f"{self.name}攻击了！")
        print("发射了556子弹")

    def being_attack(self, player):
        self.hp -= player.attack
        if self.hp < 0:
            print(f"{self.name}吃面了")
        else:
            print(f"{self.name}受伤了，剩余血量{self.hp}")


class SmallDrone(Enemy):

    def __init__(self, name=""):
        super().__init__(name)
        self.hp = 100
        self.attack = 50

    def enemy_attack(self):
        super().enemy_attack()

    def being_attack(self, player):
        super().being_attack(player)

    def moving(self):
        super().moving()


class BigDrone(Enemy):

    def __init__(self, name=""):
        super().__init__(name)
        self.hp = 200
        self.attack = 100


    def enemy_attack(self):
        super().enemy_attack()
        print("还发射了762")

    def being_attack(self, player):
        super().being_attack(player)

    def moving(self):
        super().moving()


class Boss(Enemy):

    def __init__(self, name=""):
        super().__init__(name)
        self.hp = 9999999
        self.attack = 99999999

    def enemy_attack(self):
        super().enemy_attack()
        print("还发射了天降正义")

    def being_attack(self, player):
        super().being_attack(player)

    def moving(self):
        super().moving()


player = Player("player01", 200, 200)
small_drone = SmallDrone("小飞机",)
big_drone = BigDrone("大飞机")
boss = Boss("Boss")


player.being_attacked(small_drone)
print()
player.being_attacked(big_drone)
print()
player.being_attacked(boss)
print()

small_drone.being_attack(player)
big_drone.being_attack(player)
boss.being_attack(player)
