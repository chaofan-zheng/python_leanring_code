import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个对象
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    # screen 是 一个surface, ship alien 都是一个对象
    ship = Ship(game_settings, screen)

    pygame.display.set_caption("雷霆战机")

    bullets = Group()
    aliens = Group()

    gf.create_fleet(game_settings, screen, ship, aliens)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullet(bullets,aliens)
        gf.update_aliens(game_settings,aliens)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)


if __name__ == '__main__':
    run_game()
