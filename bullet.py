import pygame
from math import sin, cos, radians
import spr_grps as sg


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SHIP_SPEED = 5
FPS = 60

WHITE = (255, 255, 255)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        pygame.sprite.Sprite.__init__(self)
        self.life_time = 0
        self.last = pygame.time.get_ticks()
        self.cooldown = 750
        self.image = pygame.Surface((10, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=pos)
        self.speedx = (SHIP_SPEED+10) * -1 * sin(radians(-angle))
        self.speedy = (SHIP_SPEED+10) * cos(radians(-angle))

    def update(self):
        self.rect.x -= self.speedx
        self.rect.y -= self.speedy
        now = pygame.time.get_ticks()
        self.life_time = now - self.last
        if self.life_time >= self.cooldown:
            self.last = now
            self.remove(sg.bullets, sg.all_sprites)
            self.kill()
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT

