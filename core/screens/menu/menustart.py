import pygame
import sys

import assets.assets
from core import setting, config, button
from core.screens.screen import Screen
from core.sound.sound import Sound


class MenuStart(Screen):
    """
        The menu that appears first when opening the application
        with two start and exit buttons
    """
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(setting.FONT_PATH, 48)

        # Create 2 buttons
        self.buttons = [
            button.btntext.btnTXT("Bắt đầu", self.font, config.YELLOW, config.BLACK, pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 330, 180, 60)),
            button.btntext.btnTXT("Thoát", self.font, config.YELLOW, config.BLACK, pygame.Rect(config.SCREEN_WIDTH // 2 - 90, 450, 180, 60))
        ]

    def draw(self):
        # self.screen.fill(config.ORANGE)
        screen_bg = pygame.image.load(assets.assets.background[1])
        screen_bg = pygame.transform.scale(screen_bg, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.screen.blit(screen_bg, (0, 0))

        # Draw logo
        logo = pygame.image.load("assets/images/logo2.png")
        logo = pygame.transform.scale(logo, (500, 200))
        title = self.font.render("POKÉMON CỔ ĐIỂN", True, config.BLACK)
        self.screen.blit(logo, (config.SCREEN_WIDTH // 2 - 250, 70))

        # Draw sound button
        self.draw_sound_button()

        # Draw 2 buttons
        # for btn in self.buttons:
        #     btn.draw(self.screen)
        # Draw button
        btn_start = pygame.image.load(assets.assets.button_path["button_play"])
        btn_start = pygame.transform.scale(btn_start, (180, 60))
        btn_exit = pygame.image.load(assets.assets.button_path["button_exit"])
        btn_exit = pygame.transform.scale(btn_exit, (180, 60))
        self.screen.blit(btn_start, (config.SCREEN_WIDTH // 2 - 90, 330))
        self.screen.blit(btn_exit, (config.SCREEN_WIDTH // 2 - 90, 450))
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sound_rect.collidepoint(event.pos): # Turn on or off volume
                self.toggle_sound()
            for btn in self.buttons: # event click different buttons
                if btn.btn["rect"].collidepoint(event.pos):
                    Sound.play_music(config.CLICK) # Play music: "click"
                    print(f"Bạn đã bấm nút {btn.btn['text']}")
                    if btn.btn_name == "Thoát": # click "Thoát" button
                        pygame.time.delay(300)
                        pygame.quit()           # quit pygame
                        sys.exit()              # close application
                    elif btn.btn_name == "Bắt đầu": # click "Bắt đầu" button
                        setting.LEVEL_OF_SCREEN = 1 # Change a different screen(