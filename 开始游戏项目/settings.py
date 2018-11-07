class Settings():
    # 屏幕参数设置
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230,230,230)

        # 设置飞机的速度
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # 设置外星人速度
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 15
        self.fleet_direction = 1





