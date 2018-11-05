import pygame
from 开始游戏项目.settings import Settings
from 开始游戏项目.ship import Ship
import 开始游戏项目.game_functions as gf
from pygame.sprite import Group
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")
    # 设置背景颜色
    # bg_color = (230,230,230)

    # 创建飞船
    ship = Ship(screen, ai_settings)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        # 调用事件发生状态
        ship.update()
        gf.update_bullets(bullets)
        # 更新屏幕，刷新
        gf.update_screen(ai_settings,screen,ship,bullets)




run_game()
