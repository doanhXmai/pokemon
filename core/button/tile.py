import pygame

from core import config
from core.ui import UI


class Tile(UI):
    def __init__(self, image_path, position, size):
        super().__init__(image_path, position)
        self.is_selected = False
        self.is_hinted = False
        self.scale(size)
        self.scope_rect(position)

    def scale(self, size):
        self.image = pygame.transform.scale(self.image, size)

    def scope_rect(self, position):
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.is_selected:
            pygame.draw.rect(screen, config.BLUE, self.rect, 3)  # Vẽ viền sáng màu xanh
        if self.is_hinted:
            overlay = pygame.Surface(self.rect.size, pygame.SRCALPHA)  # Tạo surface trong suốt
            overlay.fill((128, 128, 128, 100))  # Màu xám, độ trong suốt 100
            screen.blit(overlay, self.rect.topleft)  # Phủ lên tile