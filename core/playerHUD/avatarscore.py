import pygame

from core.ui import UI


class AvatarScore(UI):
    def __init__(self, image_path, position, score, font, name = "player"):
        super().__init__(image_path, position)
        self.name, self.score, self.font = name, score, font
        self.name_surface, self.score_surface = None, None
        self.update_text()

    def update_text(self):
        pass

    def scale(self, size):
        self.image = pygame.transform.scale(self.image, size)
        self.rect.size = size

    def scope_rect(self, position):
        pass

    def draw(self, screen):
        pass