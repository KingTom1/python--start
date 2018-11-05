import pygame

class Ship():

    def __init__(self, screen, ai_settings):
        self.screen = screen
        # ai_setting是settings类的对象
        self.ai_settings = ai_settings

        # 加载图片
        self.image = pygame.image.load('images/ship.bmp')
        # 获取图片对象rect
        self.rect = self.image.get_rect()
        # 获取屏幕对象screen_rect
        self.screen_rect = screen.get_rect()

        # 将每个飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    '''绘制飞船'''
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

