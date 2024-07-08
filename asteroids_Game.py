import pygame
import space_ship
import asteroidsf
import explosoin
import bullet
import spr_grps as sg
from necessary_funcs import asts_on_bg, text, act


pygame.init()
pygame.font.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SHIP_SPEED = 5
FPS = 100

WHITE = (255, 255, 255)
bg = pygame.image.load("bg.png")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids Game")

all_sprites = sg.all_sprites
asteroids = sg.asteroids
bullets = sg.bullets
bg_asteroids = sg.bg_asteroids


life = 3
score = 0


asts_on_bg()


ship = space_ship.Ship()
all_sprites.add(ship)
ast_arr = []
bull_arr = []
last = pygame.time.get_ticks()
cooldown_ast = 1000
for i in range(5):
    ast = asteroidsf.Asteroid('ast.gif')
    ast_arr.append(ast)
    all_sprites.add(ast)
    asteroids.add(ast)


running = True
not_waiting_mode = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bull = bullet.Bullet(ship.rect.center, ship.angle)
                bull_arr.append(bull)
                all_sprites.add(bull)
                bullets.add(bull)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 400 < pygame.mouse.get_pos()[0] < 1100 and 200 < pygame.mouse.get_pos()[1] < 700:
                not_waiting_mode = True
    if not_waiting_mode:
        hit_ast = ship.rect.collidelist([re.rect for re in ast_arr])
        if hit_ast > -1:
            life -= 1
            ship.rect = ship.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            ship.a = 1
            new_exp = explosoin.Explosion(ast_arr[hit_ast].rect.center[0], ast_arr[hit_ast].rect.center[1])
            all_sprites.add(new_exp)
            ast_arr[hit_ast].remove(all_sprites, asteroids)
            ast_arr[hit_ast].kill()
            ast_arr.pop(hit_ast)

        for bull_iter in bull_arr:
            if bull_iter.life_time >= bull_iter.cooldown:
                bull_iter.remove(all_sprites, bullets)
                bull_iter.kill()
                bull_arr.remove(bull_iter)
            hit_bull = bull_iter.rect.collidelist([re.rect for re in ast_arr])
            if hit_bull > -1:
                score += 1
                bull_iter.remove(all_sprites, bullets)
                bull_iter.kill()
                bull_arr.remove(bull_iter)

                new_exp = explosoin.Explosion(ast_arr[hit_bull].rect.center[0], ast_arr[hit_bull].rect.center[1])
                all_sprites.add(new_exp)
                ast_arr[hit_bull].remove(all_sprites, asteroids)
                ast_arr[hit_bull].kill()
                ast_arr.pop(hit_bull)

        text(screen, bg, life, score)
        act(screen)
        if life == 0:
            not_waiting_mode = False
            life = 3
            score = 0
        now = pygame.time.get_ticks()
        if now - last >= cooldown_ast:
            ast = asteroidsf.Asteroid('ast.gif')
            ast_arr.append(ast)
            all_sprites.add(ast)
            asteroids.add(ast)
            last = now
    else:
        text(screen, bg, life, score)
        sc = pygame.Surface((700, 500), pygame.SRCALPHA)
        sc.fill((0, 255, 128, 128))
        f3 = pygame.font.Font('Alpharush.ttf', 72)
        text3 = f3.render('Click to START', True,
                          (0, 180, 0))
        sc.blit(text3, (160, 300))
        bg_asteroids.update()
        bg_asteroids.draw(screen)
        screen.blit(sc, (400, 200))
        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
