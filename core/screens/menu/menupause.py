import pygame

from core import setting, config
from core.button.btntext import btnTXT
from core.screens.board import Board
from core.screens.screen import Screen
from core.sound.sound import Sound


class MenuPause(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 50)
        self.background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.background.set_alpha(180)  # Nền bán trong suốt
        self.background.fill(config.BLACK)  # Màu đen
        self.btn_continue = btnTXT("Tiếp tục", self.font, config.YELLOW, config.BLACK, pygame.Rect(380, 400, 190, 60))

    def draw(self):
        self.screen.fill(config.ORANGE)

        self.draw_sound_button()

        self.btn_continue.draw(self.screen)

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sound_rect.collidepoint(event.pos):
                self.toggle_sound()
            if self.btn_continue.btn["rect"].collidepoint(event.pos):
                print(f"Bạn đã bấm nút {self.btn_continue.btn["text"]}")
                setting.PAUSE = False
                Board.start_time += pygame.time.get_ticks() - Board.pause_time
                setting.LEVEL_OF_SCREEN = 2
                Sound.play_music(config.CLICK)