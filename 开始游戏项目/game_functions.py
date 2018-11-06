import sys
import pygame
from 开始游戏项目.bullet import Bullet
from 开始游戏项目.alien import Alien
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        # 向右飞行
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,screen,ship,bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings,screen,ship,bullets,aliens):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹,子弹出现在屏幕
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 获得飞船在屏幕刷新，飞船出现在屏幕
    ship.blitme()
    # 外星人出现在屏幕
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    # 创建子弹移动
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings,screen,aliens):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space = ai_settings.screen_width - 2*alien_width
    number_alien_x = int(available_space/(2*alien_width))

    # 创建第一行外星人
    for alien_number in range(number_alien_x):
        alien = Alien(ai_settings,screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
