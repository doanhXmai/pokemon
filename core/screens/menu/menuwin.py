import pygame

from core import setting, config
from core.screens.board import Board
from core.button.btntext import btnTXT

from core.screens.screen import Screen
from core.sound.sound import Sound


class MenuWin(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH2, 80)
        self.text = self.font.render("YOU WIN", True, config.RED)
        self.background = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        # Toạ độ trung màn hình
        center_x = config.SCREEN_WIDTH // 2
        center_y = config.SCREEN_HEIGHT // 2
        # căn giữa chữ "Bạn đã WIN"
        self.text_rect = self.text.get_rect(center = (center_x, center_y - 120))

        # font chữ cho các nút
        btn_font = pygame.font.Font(None, 40)
        # Nút "Tiếp tục"
        self.btn_continue = btnTXT("Tiếp tục", btn_font, config.GREEN, config.WHITE,
                                   pygame.Rect(center_x - 75, center_y - 10, 150, 60))
        # Nút trở về
        self.btn_back = btnTXT("Trở về", btn_font, config.RED, config.WHITE,
                               pygame.Rect(center_x - 75, center_y + 100, 150, 60))

    def draw(self):
        #draw bg
        screen_bg = pygame.image.load("assets/images/background1.jpg")
        screen_bg = pygame.transform.scale(screen_bg, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.screen.blit(screen_bg, (0,0))

        self.screen.blit(self.text, self.text_rect)

        #draw button
        btn_continue = pygame.image.load("assets/images/btn_tryagain.png")
        btn_continue = pygame.transform.scale(btn_continue, (150, 60))
        btn_exit = pygame.image.load("assets/images/btn_back3.png")
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
                setting.LEVEL_OF_SCREEN = 2  # Quay lại màn chơi
                Board.start_time = pygame.time.get_ticks()
                Board.pause_time = 0
                Sound.sound_manager.play_sound(config.CLICK)
                print(f"Tiếp tục chơi màn {setting.LEVEL}")

            elif self.btn_back.btn["rect"].collidepoint(event.pos):
                setting.LEVEL_OF_SCREEN = 1  # Quay về menu chính
                Sound.sound_manager.play_sound(config.CLICK)
                print("Quay về menu chính")