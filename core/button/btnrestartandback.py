import pygame

from core import setting, config
from core.button.btntext import btnTXT


class btnRestartAndBack:
    def __init__(self):
        self.font = pygame.font.Font(setting.FONT_PATH, 50)
        self.buttons = [
            btnTXT("Restart", self.font, config.RED, config.WHITE,
                   pygame.Rect(10, config.SCREEN_HEIGHT - 90, 150, 60)),
            btnTXT("Back", self.font, config.RED, config.WHITE,
                   pygame.Rect(config.SCREEN_WIDTH - 160, config.SCREEN_HEIGHT - 90, 150, 60))
        ]

    def draw(self, screen):
        for btn in self.buttons:
            btn.draw(screen)
