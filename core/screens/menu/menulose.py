import pygame

import assets.assets
from core import setting, config, button, screens, sound
from core.screens.boards.board import Board
from core.screens.screen import Screen

class MenuLose(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 40)
        self.text = pygame.font.Font(setting.FONT_PATH, 80).render("YOU LOSE", True, config.RED)
        self.text_total_score = self.font.render(f"Tổng điểm đã đạt: {Board.total_score}", True, config.WHITE)
        self.background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        # Toạ độ trung màn hình
        center_x = config.SCREEN_WIDTH // 2
        center_y = config.SCREEN_HEIGHT // 2
        self.text_rect = self.text.get_rect(center=(center_x, center_y - 150))
        self.text_total_score_rect = self.text_total_score.get_rect(center=(center_x, center_y - 100))

        # Nút "Tiếp tục"
        self.btn_continue = button.btntext.btnTXT("Tiếp tục", self.font, config.GREEN, config.WHITE,
                                   pygame.Rect(center_x - 75, center_y - 10, 150, 60))
        # Nút trở về
        self.btn_back = button.btntext.btnTXT("Trở về", self.font, config.RED, config.WHITE,
                               pygame.Rect(center_x - 75, center_y + 100, 150, 60))

    def draw(self):
        # self.screen.fill(config.ORANGE)
        screen_bg = pygame.image.load(assets.assets.background[0])
        screen_bg = pygame.transform.scale(screen_bg, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.screen.blit(screen_bg, (0, 0))
        self.text_total_score = self.font.render(f"Tổng điểm đã đặt: {Board.total_score}", True, config.WHITE)
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.text_total_score, self.text_total_score_rect)

        # draw button
        btn_continue = pygame.image.load(assets.assets.button_path["btn_tryagain"])
        btn_continue = pygame.transform.scale(btn_continue, (150, 60))
        btn_exit = pygame.image.load(assets.assets.button_path["btn_back2"])
        btn_exit = pygame.transform.scale(btn_exit, (150, 60))
        self.screen.blit(btn_continue, (config.SCREEN_WIDTH // 2 - 75, config.SCREEN_HEIGHT // 2 - 10))
        self.screen.blit(btn_exit, (config.SCREEN_WIDTH // 2 - 75, config.SCREEN_HEIGHT // 2 + 100))

        self.draw_sound_button()
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sound_rect.collidepoint(event.pos):
                self.toggle_sound()
            if self.btn_continue.btn["rect"].collidepoint(event.pos):
                Board.level = 1  # Chuyển về level 1
                print(f"Bạn có muốn chơi lại")
                screens.boards.board.Board.back = True
                Board.total_score = 0
                Board.score = 10 * Board.level
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