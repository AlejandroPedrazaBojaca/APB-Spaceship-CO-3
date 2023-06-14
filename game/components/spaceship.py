import pygame
from pygame.sprite import Sprite



from game.utils.constants import SPACESHIP

class Spaceship(Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500

    def update(self):
        pass

    def draw(self, screen):
       screen.blit(self.image, (self.rect.x, self.rect.y))
