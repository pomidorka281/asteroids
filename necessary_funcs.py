import pygame
import asteroidsf
from spr_grps import all_sprites, bg_asteroids
import random


pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800


def act(screen):
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)


def text(screen, bg, num_of_lives=3, num_of_score=0):
    f1 = pygame.font.Font('Alpharush.ttf', 72)
    text1 = f1.render('Lives ' + str(num_of_lives), True,
                      (0, 180, 0))
    f2 = pygame.font.Font('Alpharush.ttf', 72)
    text2 = f2.render('Score ' + str(num_of_score), True,
                      (0, 180, 0))
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(text1, (100, 50))
    screen.blit(text2, (1100, 50))


def asts_on_bg():
    ast_on_bg_arr = []
    for i in range(20):
        ast = asteroidsf.Asteroid('ast_50.png')
        ast.speedx = -5
        ast.speedy = 0
        ast_on_bg_arr.append(ast)
        all_sprites.add(ast)
        bg_asteroids.add(ast)


def pos():
    x, y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
    while 400 < x < 1100 and 200 < y < 700:
        x, y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
    return x, y
