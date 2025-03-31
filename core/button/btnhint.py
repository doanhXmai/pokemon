import pygame

from core.ui import UI


class btnHint(UI):
    def __init__(self, image_path, position):
        super().__init__(image_path, position)
        self.scale((40, 40))
        self.scope_rect(position)

    def scale(self, size):
        self.image = pygame.transform.scale(self.image, size=(40, 40))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def scope_rect(self, position):
        self.rect = self.image.get_rect()
        self.rect.center = position