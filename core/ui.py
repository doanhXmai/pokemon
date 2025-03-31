from abc import ABC, abstractmethod

import pygame.image


class UI(ABC):
    def __init__(self, image_path, position):
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.rect = None

    @abstractmethod
    def scale(self, size):
        pass

    @abstractmethod
    def scope_rect(self, position):
        pass

    @abstractmethod
    def draw(self, screen):
        pass
