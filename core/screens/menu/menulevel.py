import pygame

import assets.assets
from core import setting, config, button, sound
from core.screens.screen import Screen


class MenuLevel(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 48)

        # Nút quay lại
        self.back_icon = pygame.image.load(assets.assets.button_path["btn_back1"])
        self.back_icon = pygame.transform.scale(self.back_icon, (40, 40))
        self.back_rect = self.back_icon.get_rect(topleft=(10, 10))

        self.buttons = [
            button.btntext.btnTXT("Chơi đơn", self.font, config.LIGHT_PINK, config.ORANGE,
                                  pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 150, 220, 80)),
            button.btntext.btnTXT("Chơi với máy", self.font, config.LIGHT_PINK, config.DODGER_BLUE,
                                  pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 270, 220, 80)),
            button.btntext.btnTXT("Tập luyện", self.font, config.LIGHT_PINK, config.LIME_GREEN,
                                  pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 390, 220, 80))
        ]



    def draw(self):
        # draw background
        screen_bg = pygame.image.load(assets.assets.background[2])
        screen_bg = pygame.transform.scale(screen_bg, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.screen.blit(screen_bg, (0, 0))

        # Vẽ nút quay lại
        self.screen.blit(self.back_icon, self.back_rect)

        # Vẽ nút âm thanh
        self.draw_sound_button()

        btn_training = pygame.image.load(assets.assets.button_path["btn_training"])
        btn_training = pygame.transform.scale(btn_training, (220, 80))
        btn_player_vs_bot = pygame.image.load(assets.assets.button_path["btn_playervsbot"])
        btn_player_vs_bot = pygame.transform.scale(btn_player_vs_bot, (220, 80))
        btn_multiplayer = pygame.image.load(assets.assets.button_path["btn_multiplayer"])
        btn_multiplayer = pygame.transform.scale(btn_multiplayer, (220, 80))

        self.screen.blit(btn_training, (config.SCREEN_WIDTH // 2 - 90, 150))
        self.screen.blit(btn_player_vs_bot, (config.SCREEN_WIDTH // 2 - 90, 270))
        self.screen.blit(btn_multiplayer, (config.SCREEN_WIDTH // 2 - 90, 390))

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
                    if btn.btn_name == "Chơi đơn":
                        setting.LEVEL_OF_SCREEN = 2
                    elif btn.btn_name == "Chơi với máy":
                        setting.LEVEL_OF_SCREEN = 3
                    elif btn.btn_name == "Tập luyện":
                        setting.LEVEL_OF_SCREEN = 7
                    sound.sound.Sound.play_music(config.CLICK)
