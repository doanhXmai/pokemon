from abc import ABC, abstractmethod

import pygame.image

from core import setting, config


class Screen(ABC):
    def __init__(self, screen):
        self.screen = screen

        # Nút âm thanh
        self.sound_icon = pygame.image.load("assets/images/btn_mute.png")
        self.sound_icon = pygame.transform.scale(self.sound_icon, size=(40, 40))
        self.sound_rect = self.sound_icon.get_rect(topright = (config.SCREEN_WIDTH - 10, 10))

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass

    def toggle_sound(self):
        setting.TURN_ON_VOLUME = not setting.TURN_ON_VOLUME
        self.draw_sound_button()

    def draw_sound_button(self):
        sound_path = "assets/images/btn_unmute.png" if setting.TURN_ON_VOLUME else "assets/images/btn_mute.png"
        self.sound_icon = pygame.image.load(sound_path)
        self.sound_icon = pygame.transform.scale(self.sound_icon, (40, 40))
        self.screen.blit(self.sound_icon, self.sound_rect)