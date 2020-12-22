import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()  # 获取image 的 属性rectangle,python用处理矩形的方法处理surface

        # 大致在左上角生成敌人飞机
        # 敌人飞机的生成位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.game_settings.alien_speed_factor *self.game_settings.fleet_direction)# 经过更新的左上角
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

