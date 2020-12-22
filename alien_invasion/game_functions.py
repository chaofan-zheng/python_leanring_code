import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(game_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, game_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(game_settings, screen, ship, aliens, bullets):
    screen.fill(game_settings.bg_color)
    for bullets in bullets.sprites():
        bullets.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullet(bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(game_settings, screen, ship, aliens):
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_alien_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)


def get_number_alien_x(game_settings, alien_width):
    avaliable_space_x = game_settings.screen_width - 2 * alien_width
    numer_aliens_x = int(avaliable_space_x / (2 * alien_width))
    return numer_aliens_x


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(game_settings, ship_height, alien_height):
    avaliable_space_y = (game_settings.screen_height - 3 * alien_height - ship_height)
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows


def update_aliens(game_settings, aliens):
    check_fleet_edges(game_settings, aliens)
    aliens.update()


def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def check_fleet_edges(game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break
