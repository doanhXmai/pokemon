import pygame

from core import setting, config
from core.screens.screen import Screen
from core.sound.sound import Sound


class MenuLevel(Screen):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 48)

        
        # Nút quay lại
        self.back_icon = pygame.image.load("assets/images/btn_back2.png")
        self.back_icon = pygame.transform.scale(self.back_icon, (50, 40))
        self.back_rect = self.back_icon.get_rect(topleft=(10, 10))

        # Danh sách các nút chọn chế độ chơi
        self.buttons = [
            {"text": "Tập luyện", "color": (255, 182, 193), "text_color": (255, 165, 0),
             "rect": pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 150, 220, 80)},
            {"text": "Chơi với máy", "color": (255, 182, 193), "text_color": (30, 144, 255),
             "rect": pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 270, 220, 80)},
            {"text": "Chơi với người", "color": (255, 182, 193), "text_color": (50, 205, 50),
             "rect": pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 390, 220, 80)}
        ]



    def draw(self):

        #draw background
        screen_bg = pygame.image.load("assets/images/background4.png")
        screen_bg = pygame.transform.scale(screen_bg, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.screen.blit(screen_bg, (0,0))
        # Vẽ nút quay lại
        self.screen.blit(self.back_icon, self.back_rect)

        # Vẽ nút âm thanh
        self.draw_sound_button()

        # Vẽ các nút
        # for btn in self.buttons:
        #     pygame.draw.rect(self.screen, btn["color"], btn["rect"], border_radius=15)
        #     text_surface = self.font.render(btn["text"], True, btn["text_color"])
        #     text_x = btn["rect"].x + (btn["rect"].width - text_surface.get_width()) // 2
        #     text_y = btn["rect"].y + (btn["rect"].height - text_surface.get_height()) // 2
        #     self.screen.blit(text_surface, (text_x, text_y))

        btnTraining = pygame.image.load("assets/images/btn_training.png")
        btnTraining = pygame.transform.scale(btnTraining, (220, 80))
        btnPlayervsbot = pygame.image.load("assets/images/btn_playervsbot.png")
        btnPlayervsbot = pygame.transform.scale(btnPlayervsbot, (220, 80))
        btnMultiplayer = pygame.image.load("assets/images/btn_multiplayer.png")
        btnMultiplayer = pygame.transform.scale(btnMultiplayer, (220, 80))

        self.screen.blit(btnTraining, (config.SCREEN_WIDTH // 2 - 90, 150))
        self.screen.blit(btnPlayervsbot, (config.SCREEN_WIDTH // 2 - 90, 270))
        self.screen.blit(btnMultiplayer, (config.SCREEN_WIDTH // 2 - 90, 390))
    
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sound_rect.collidepoint(event.pos): # Sự kiện click nút âm thanh
                self.toggle_sound()
            if self.back_rect.collidepoint(event.pos):
                print("Quay lại menu chính")
                setting.LEVEL_OF_SCREEN = 0
            for btn in self.buttons:
                if btn["rect"].collidepoint(event.pos):
                    print(f"Bạn đã chọn: {btn['text']}")
                    if btn["text"] == "Tập luyện":
                        setting.LEVEL_OF_SCREEN = 2
                    Sound.sound_manager.play_sound(config.CLICK)
