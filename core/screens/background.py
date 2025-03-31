import pygame

from core import config


class Background:
    @staticmethod
    def load_image(image_path, size = (config.SCREEN_WIDTH, config.SCREEN_HEIGHT)):
        background = pygame.image.load(image_path)
        return Background.scale(background, size)
    @staticmethod
    def scale(background, size):
        return pygame.transform.scale(background, size)