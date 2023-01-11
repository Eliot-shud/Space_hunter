import pygame, sys
from bullet import Bullet
from nerons import Neron
import time

def events(screen, gun, bullets):
    """ события """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # движение вправо
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # движение вправо
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = True

def update(bg_color, screen, stats, sc, gun, nerons, bullets):
    """ Обновление частоты экрана """
    screen.fill(bg_color)
    sc.show.score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    nerons.draw(screen)
    pygame.display.flip()

def update_bullets(screen, sc, stats, nerons, bullets):
    """ Изменение позиции пуль """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, nerons, True, True)
    if collisions:
        for nerons in collisions.values():
            stats.score += 10 * len(nerons)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(nerons) == 0:
        bullets.empty()
        create_army(screen, nerons)

def gun_kill(stats, screen, sc, gun, nerons, bullets):
    """Столкновение армии и пушки"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        nerons.empty()
        bullets.empty()
        create_army(screen, nerons)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, sc, gun, nerons, bullets):
    """Наступленее инопрещеленьцев"""
    nerons.update()
    if pygame.sprite.spritecollideany(gun, nerons):
        gun_kill(stats, screen, sc, gun, nerons, bullets)
    nerons_check(stats, screen, sc, gun, nerons, bullets)

def nerons_check(stats, screen, sc, gun, nerons, bullets):
    """проверка перезагрузки игры"""
    screen_rect = screen.get_rect()
    for nerons in nerons.sprites():
        if nerons.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, nerons, bullets)
            break

def create_army(screen, nerons):
    """Создание армии захватчиков"""
    nerons = Neron(screen)
    nerons_width = nerons.rect.width
    number_nerons_x = int((700 - 2 * nerons_width) / nerons_width)
    neron_height = nerons.rect.height
    number_nerons_y = int((800 - 100 - 2 * neron_height) / neron_height)

    for row_number in range(number_nerons_y - 1):
        for nerons_number in range(number_nerons_x):
            nerons = Neron(screen)
            nerons.x = nerons_width + (nerons_width * nerons_number)
            nerons.y = neron_height + (neron_height * row_number)
            nerons.rect.x = nerons.x
            nerons.rect.y = nerons.rect.height + (nerons.rect.height * row_number)
            nerons.add(nerons)

def check_high_score(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as file:
            file.write(str(stats.high_score))



