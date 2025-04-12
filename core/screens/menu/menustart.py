import pygame
import sys

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
            button.btntext.btnTXT("Bắt đầu", self.font, config.YELLOW, config.BLACK, pygame.Rect(270, 400, 180, 60)),
            button.btntext.btnTXT("Thoát", self.font, config.YELLOW, config.BLACK, pygame.Rect(580, 400, 180, 60))
        ]

    def draw(self):
        self.screen.fill(config.ORANGE)

        # Draw logo
        title = self.font.render("POKÉMON CỔ ĐIỂN", True, config.BLACK)
        self.screen.blit(title, (config.SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        # Draw sound button
        self.draw_sound_button()

        # Draw 2 buttons
        for btn in self.buttons:
            btn.draw(self.screen)

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