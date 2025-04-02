import pygame

from core import setting, config, button, screens, sound
from core.screens.screen import Screen

class MenuLose(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 40)
        self.text = pygame.font.Font(None, 80).render("Bạn đã LOSE", True, config.BLACK)
        self.text_total_score = self.font.render(f"Tổng điểm đã đặt: {setting.TOTAL_SCORE}", True, config.BLACK)
        self.background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        # Toạ độ trung màn hình
        center_x = config.SCREEN_WIDTH // 2
        center_y = config.SCREEN_HEIGHT // 2
        # căn giữa chữ "Bạn đã WIN"
        self.text_rect = self.text.get_rect(center=(center_x, center_y - 100))

        # font chữ cho các nút
        btn_font = pygame.font.Font(None, 40)
        # Nút "Tiếp tục"
        self.btn_continue = button.btntext.btnTXT("Tiếp tục", btn_font, config.GREEN, config.WHITE,
                                   pygame.Rect(center_x - 100, center_y, 200, 50))
        # Nút trở về
        self.btn_back = button.btntext.btnTXT("Trở về", btn_font, config.RED, config.WHITE,
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
                setting.LEVEL = 1  # Chuyển về level 1
                print(f"Bạn có muốn chơi lại")
                screens.boards.board.Board.back = True
                setting.TOTAL_SCORE = 0
                setting.SCORE = 10 * setting.LEVEL
                setting.LEVEL_OF_SCREEN = 2  # Quay lại màn chơi
                setting.LOSE = False
                screens.boards.boardsolo.BoardOfSolo.pause_time = 0
                screens.boards.boardsolo.BoardOfSolo.start_time = pygame.time.get_ticks()
                sound.sound.Sound.play_music(config.CLICK)

            elif self.btn_back.btn["rect"].collidepoint(event.pos):
                print("Quay về menu chính")
                screens.boards.board.Board.back = True
                setting.LEVEL_OF_SCREEN = 1  # Quay về menu chính
                sound.sound.Sound.play_music(config.CLICK)