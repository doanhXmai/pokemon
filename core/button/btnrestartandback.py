import pygame

from core import setting, config, button


class btnRestartAndBack:
    def __init__(self):
        self.font = pygame.font.Font(setting.FONT_PATH, 50)
        self.buttons = [
            button.btntext.btnTXT("Restart", self.font, config.RED, config.WHITE,
                   pygame.Rect(25, config.SCREEN_HEIGHT - 80, 120, 50)),
            button.btntext.btnTXT("Back", self.font, config.RED, config.WHITE,
                   pygame.Rect(config.SCREEN_WIDTH - 145, config.SCREEN_HEIGHT - 80, 120, 50))
        ]

    def draw(self, screen):
        for btn in self.buttons:
            btn.draw(screen)