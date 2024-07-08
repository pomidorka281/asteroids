import pygame
from math import sin, cos, radians
import spr_grps as sg


all_sprites = sg.all_sprites
asteroids = sg.asteroids
bullets = sg.bullets


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SHIP_SPEED = 5
FPS = 60

WHITE = (255, 255, 255)


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ship2_no_fire.gif')
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.angle = 0
        self.a = 1
        self.ship_speed = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5
        self.image = pygame.transform.rotozoom(pygame.image.load('ship2_no_fire.gif'), self.angle, 1)
        if keys[pygame.K_UP]:
            self.rect.x -= (self.ship_speed + self.a) * -1 * sin(radians(-self.angle))
            self.rect.y -= (self.ship_speed + self.a) * cos(radians(-self.angle))
            self.image = pygame.transform.rotozoom(pygame.image.load('ship2.gif'), self.angle, 1)
        if not keys[pygame.K_UP]:
            self.rect.x -= (self.ship_speed + self.a) * -1 * sin(radians(-self.angle))
            self.rect.y -= (self.ship_speed + self.a) * cos(radians(-self.angle))
            self.image = pygame.transform.rotozoom(pygame.image.load('ship2_no_fire.gif'), self.angle, 1)
        if keys[pygame.K_UP]:
            self.a += 1
            if self.a > 15:
                self.a = 15
        if not keys[pygame.K_UP]:
            self.a -= 1
            if self.a <= 0:
                self.a = 0
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
