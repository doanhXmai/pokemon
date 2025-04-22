import pygame

from core.ui import UI

class btnPause(UI):
    def __init__(self, image_path, position):
        super().__init__(image_path, position)
        self.scale((45, 35))
        self.scope_rect(position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def scope_rect(self, position):
        self.rect = self.image.get_rect()
        self.rect.center = position

    def scale(self, size):
        self.image = pygame.transform.scale(self.image, size=(45, 35))