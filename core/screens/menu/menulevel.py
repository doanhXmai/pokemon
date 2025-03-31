import pygame

from core import setting, config, button
from core.screens.screen import Screen
from core.sound.sound import Sound


class MenuLevel(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 48)

        # Nút quay lại
        self.back_icon = pygame.image.load("assets/images/back.png")
        self.back_icon = pygame.transform.scale(self.back_icon, (40, 40))
        self.back_rect = self.back_icon.get_rect(topleft=(10, 10))

        self.buttons = [
            button.btntext.btnTXT("Tập luyện", self.font, config.LIGHT_PINK, config.ORANGE,
                                  pygame.Rect((config.SCREEN_WIDTH - 400) // 2, 200, 400, 60)),
            button.btntext.btnTXT("Chơi với máy", self.font, config.LIGHT_PINK, config.DODGER_BLUE,
                                  pygame.Rect((config.SCREEN_WIDTH - 400) // 2, 300, 400, 60)),
            button.btntext.btnTXT("Chơi với người", self.font, config.LIGHT_PINK, config.LIME_GREEN,
                                  pygame.Rect((config.SCREEN_WIDTH - 400) // 2, 400, 400, 60))
        ]



    def draw(self):
        self.screen.fill((173, 216, 230))  # Màu nền xanh nhạt

        # Vẽ nút quay lại
        self.screen.blit(self.back_icon, self.back_rect)

        # Vẽ nút âm thanh
        self.draw_sound_button()

        # Vẽ các nút
        for btn in self.buttons:
            btn.draw(self.screen)

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sound_rect.collidepoint(event.pos): # Sự kiện click nút âm thanh
                self.toggle_sound()
            if self.back_rect.collidepoint(event.pos):
                print("Quay lại menu chính")
                setting.LEVEL_OF_SCREEN = 0
            for btn in self.buttons:
                if btn.btn["rect"].collidepoint(event.pos):
                    print(f"Bạn đã chọn: {btn.btn['text']}")
                    if btn.btn_name == "Tập luyện":
                        setting.LEVEL_OF_SCREEN = 2
                    Sound.play_music(config.CLICK)
