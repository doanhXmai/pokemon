import pygame

import assets.assets
from core import setting, config, button
from board import Board
from core.screens.screen import Screen
from core.screens.boards.boardsolo import BoardOfSolo
from core.sound.sound import Sound


class MenuPause(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 50)
        self.background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.background.set_alpha(180)  # Nền bán trong suốt
        self.background.fill(config.BLACK)  # Màu đen
        self.btn_continue = button.btntext.btnTXT("Tiếp tục", self.font, config.YELLOW, config.BLACK, pygame.Rect(380, 400, 190, 60))

    def draw(self):
        # draw background
        screen_bg = pygame.image.load(assets.assets.background[3])
        screen_bg = pygame.transform.scale(screen_bg, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.screen.blit(screen_bg, (0, 0))

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
                BoardOfSolo.start_time += pygame.time.get_ticks() - BoardOfSolo.pause_time
                setting.LEVEL_OF_SCREEN = 2
                Sound.play_music(config.CLICK)