import pygame

from bot.core.bot import Bot
from core import setting, config, button
from core.screens.boards.board import Board
from core.screens.boards.boardBot import BoardBattleBot
from core.screens.screen import Screen
from core.sound.sound import Sound


class GameOver(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 80)
        self.background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        # Toạ độ trung màn hình
        self.center_x = config.SCREEN_WIDTH // 2
        self.center_y = config.SCREEN_HEIGHT // 2
        # căn giữa chữ "Bạn đã WIN"

        # font chữ cho các nút
        self.btn_font = pygame.font.Font(setting.FONT_PATH, 40)
        # Nút "Tiếp tục"
        self.btn_continue = button.btntext.btnTXT("Tiếp tục", self.btn_font, config.GREEN, config.WHITE,
                                                  pygame.Rect(self.center_x - 100, self.center_y, 200, 50))
        # Nút trở về
        self.btn_back = button.btntext.btnTXT("Trở về", self.btn_font, config.RED, config.WHITE,
                                              pygame.Rect(self.center_x - 100, self.center_y + 80, 200, 50))

    def draw(self):
        text = self.font.render("Bạn đã chiến thắng" if Board.total_score > Bot.score else "Bạn đã thua", True,
                                     config.BLACK)
        text_rect = text.get_rect(center=(self.center_x, self.center_y - 100))
        self.screen.fill(config.ORANGE)
        self.screen.blit(text, text_rect)
        self.btn_continue.draw(self.screen)
        self.btn_back.draw(self.screen)

        self.draw_sound_button()
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sound_rect.collidepoint(event.pos):
                self.toggle_sound()
            if self.btn_continue.btn["rect"].collidepoint(event.pos):
                setting.LEVEL_OF_SCREEN = 3
                Sound.play_music(config.CLICK)
                Board.back = True
                BoardBattleBot.game_over = False
                Board.total_score = 0
                Bot.score = 0
                print(f"Tiếp tục chơi lại")

            elif self.btn_back.btn["rect"].collidepoint(event.pos):
                setting.LEVEL_OF_SCREEN = 1  # Quay về menu chính
                Sound.play_music(config.CLICK)
                Board.back = True
                BoardBattleBot.game_over = False
                Board.total_score = 0
                Bot.score = 0
                print("Quay về menu chính")