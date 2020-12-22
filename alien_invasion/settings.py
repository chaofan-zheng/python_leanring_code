"""存储雷霆战机的所有类"""


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.speed_factor = 1.5
        self.bullet_speed_factor = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 255, 255, 102
        self.bullets_allowed = 5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction =1 表示右移动，-1表示左移
        self.fleet_direction = 1
