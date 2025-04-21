import pygame

from core import config
from core.ui import UI


class btnPause(UI):
    def __init__(self, image_path, position):
        super().__init__(image_path, position)
        self.scale((35, 35))
        self.scope_rect((config.SCREEN_WIDTH // 2 + 4, 26))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def scope_rect(self, position):
        # self.rect.center = position
        self.rect = self.image.get_rect()
        self.rect.center = position

    def handle_event(self, event):
        pass
    def scale(self, size):
        self.image = pygame.transform.scale(self.image, size=(45, 35))