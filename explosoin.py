import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('explode.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.last = pygame.time.get_ticks()
        self.cooldown = 300

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            self.kill()
