import pygame
import random
from necessary_funcs import pos


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SHIP_SPEED = 5
FPS = 60

WHITE = (255, 255, 255)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.image = pygame.image.load(self.img)
        self.rect = self.image.get_rect(center=(pos()))
        self.speedx = random.randint(-5, 5)
        self.speedy = random.randint(-5, 5)
        self.angle = random.randint(1, 4)
        self.rot_speed = random.randint(1, 5)

    def update(self):
        self.angle += self.rot_speed
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = SCREEN_HEIGHT
        self.image = pygame.transform.rotozoom(pygame.image.load(self.img), self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
