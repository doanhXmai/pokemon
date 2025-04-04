import pygame

from core import setting, config, button, screens
from board import Board
from core.screens.screen import Screen
from core.screens.boards.boardsolo import BoardOfSolo
from core.sound.sound import Sound


class MenuWin(Screen):
    isSolo = False
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 80)
        self.text = self.font.render(f"Bạn đã WIN", True, config.BLACK)
        self.background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        # Toạ độ trung màn hình
        center_x = config.SCREEN_WIDTH // 2
        center_y = config.SCREEN_HEIGHT // 2
        # căn giữa chữ "Bạn đã WIN"
        self.text_rect = self.text.get_rect(center = (center_x, center_y - 100))

        # font chữ cho các nút
        self.btn_font = pygame.font.Font(setting.FONT_PATH, 40)
        # Nút "Tiếp tục"
        self.btn_continue = button.btntext.btnTXT("Tiếp tục", self.btn_font, config.GREEN, config.WHITE,
                                   pygame.Rect(center_x - 100, center_y, 200, 50))
        # Nút trở về
        self.btn_back = button.btntext.btnTXT("Trở về", self.btn_font, config.RED, config.WHITE,
                               pygame.Rect(center_x - 100, center_y + 80, 200, 50))

    def draw(self):
        self.screen.fill(config.ORANGE)
        self.screen.blit(self.text, self.text_rect)
        self.btn_continue.draw(self.screen)
        self.btn_back.draw(self.screen)

        self.draw_sound_button()
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sound_rect.collidepoint(event.pos):
                self.toggle_sound()
            if self.btn_continue.btn["rect"].collidepoint(event.pos):
                if MenuWin.isSolo:
                    setting.LEVEL_OF_SCREEN = 2  # Quay lại màn chơi
                    BoardOfSolo.start_time = pygame.time.get_ticks()
                    BoardOfSolo.pause_time = 0
                else:
                    setting.LEVEL_OF_SCREEN = 7
                Sound.play_music(config.CLICK)
                screens.boards.board.Board.back = True
                print(f"Tiếp tục chơi màn {setting.LEVEL}")

            elif self.btn_back.btn["rect"].collidepoint(event.pos):
                setting.LEVEL_OF_SCREEN = 1  # Quay về menu chính
                Sound.play_music(config.CLICK)
                screens.boards.board.Board.back = True
                print("Quay về menu chính")