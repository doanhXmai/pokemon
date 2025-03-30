import pygame
import sys

from core import setting, config
from core.button.btntext import btnTXT
from core.screens.screen import Screen
from core.sound.sound import Sound


class MenuStart(Screen):

    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 48)

        self.buttons = [
            btnTXT("Bắt đầu", self.font, config.YELLOW, config.BLACK, pygame.Rect(270, 400, 180, 60)),
            btnTXT("Thoát", self.font, config.YELLOW, config.BLACK, pygame.Rect(580, 400, 180, 60))
        ]

    def draw(self):
        self.screen.fill(config.ORANGE)

        # Draw logo
        title = self.font.render("POKÉMON CỔ ĐIỂN", True, config.BLACK)
        self.screen.blit(title, (config.SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        # Draw sound button
        self.draw_sound_button()

        # Draw button
        for btn in self.buttons:
            btn.draw(self.screen)

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sound_rect.collidepoint(event.pos): # Sự kiện click nút âm thanh
                self.toggle_sound()
            for btn in self.buttons:
                if btn.btn["rect"].collidepoint(event.pos):
                    Sound.sound_manager.play_sound(config.CLICK)
                    print(f"Bạn đã bấm nút {btn.btn['text']}")
                    if btn.btn_name == "Thoát":
                        pygame.quit()
                        sys.exit()
                    elif btn.btn_name == "Bắt đầu":
                        setting.LEVEL_OF_SCREEN = 1