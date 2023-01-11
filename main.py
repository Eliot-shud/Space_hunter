import pygame, controls
from plasm_gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space hunter")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group
    nerons = Group()
    controls.create_army(screen, nerons)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, nerons, bullets)
            controls.update_bullets(screen, stats, sc, nerons, bullets)
            controls.update_inos(stats, screen, sc, gun, nerons, bullets)

run()













