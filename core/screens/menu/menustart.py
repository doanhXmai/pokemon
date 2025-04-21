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
            btnTXT("Bắt đầu", self.font, config.GRAY, config.BLACK, pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 330, 180, 60)),
            btnTXT("Thoát", self.font, config.GRAY, config.BLACK, pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 450, 180, 60))
        ]

    def draw(self):
        
        # Draw background
        screen_bg = pygame.image.load("assets/images/background2.jpg")
        screen_bg = pygame.transform.scale(screen_bg, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.screen.blit(screen_bg, (0,0))

        # Draw logo
        logo = pygame.image.load("assets/images/logo2.png")
        logo = pygame.transform.scale(logo, (500,200))
        title = self.font.render("POKÉMON CỔ ĐIỂN", True, config.BLACK)
        self.screen.blit(logo, (config.SCREEN_WIDTH // 2 - 250, 70))

        # Draw sound button
        self.draw_sound_button()

        # Draw button
        btnStart = pygame.image.load("assets/images/button_play.png")
        btnStart = pygame.transform.scale(btnStart, (180, 60))
        btnExit = pygame.image.load("assets/images/button_exit.png")
        btnExit = pygame.transform.scale(btnExit, (180, 60))

        self.screen.blit(btnStart, (config.SCREEN_WIDTH // 2 - 90, 330))
        self.screen.blit(btnExit, (config.SCREEN_WIDTH // 2 - 90, 450))


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