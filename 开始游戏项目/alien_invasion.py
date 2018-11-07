import pygame
from 开始游戏项目.settings import Settings
from 开始游戏项目.ship import Ship
import 开始游戏项目.game_functions as gf
from pygame.sprite import Group
from 开始游戏项目.alien import Alien

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # 属性控制的对象
    ai_settings = Settings()
    # 获取一个屏幕 对象
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # # 创建一个外星人
    # alien = Alien(ai_settings, screen)

    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship = Ship(screen, ai_settings)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)


    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        # 调用事件发生状态
        ship.update()
        gf.update_bullets(bullets,aliens,ai_settings,screen,ship)
        gf.update_aliens(ai_settings,aliens)
        # 更新屏幕，刷新
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)

run_game()
