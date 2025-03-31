import sys
import pygame

from core import setting, config
from core.screens import menu
from core.screens.board import Board
from core.sound.sound import Sound


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Pokémon Nối hình")
        Sound.load_sound()

        # screen menus
        self.menu_start = menu.menustart.MenuStart(self.screen)
        self.menu_level = menu.menulevel.MenuLevel(self.screen)
        self.menu_pause = menu.menupause.MenuPause(self.screen)
        self.menu_win = menu.menuwin.MenuWin(self.screen)
        self.menu_lose = menu.menulose.MenuLose(self.screen)

        # screen main
        self.board = None

        # condition to start game loop
        self.running = True

    def run(self):
        """Game loop"""
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            # Chỉ xử lý sự kiện của menu hiện tại
            if setting.LEVEL_OF_SCREEN == 0:
                self.menu_start.handle_event(event)
            elif setting.LEVEL_OF_SCREEN == 1:
                self.menu_level.handle_event(event)
            elif setting.LEVEL_OF_SCREEN == 2:
                self.board.handle_event(event)
            elif setting.LEVEL_OF_SCREEN == 4:
                self.menu_pause.handle_event(event)
            elif setting.LEVEL_OF_SCREEN == 5:
                self.menu_win.handle_event(event)
            elif setting.LEVEL_OF_SCREEN == 6:
                self.menu_lose.handle_event(event)

    def draw(self):
        if setting.LEVEL_OF_SCREEN == 0:
            self.menu_start.draw()  # Vẽ menu start
        elif setting.LEVEL_OF_SCREEN == 1:
            self.menu_level.draw()  # Vẽ menu level
            self.board = Board(self.screen)
        elif setting.LEVEL_OF_SCREEN == 2:
            self.board.draw()
            if setting.LOSE:
                Sound.play_music(config.LOSE)
                setting.LEVEL_OF_SCREEN = 6
                setting.LOSE = False
            if setting.WIN:
                setting.LEVEL += 1  # Chuyển sang level tiếp theo
                setting.SCORE = 10 * setting.LEVEL
                setting.LEVEL_OF_SCREEN = 5
                Sound.play_music(config.WIN)
                setting.WIN = False
        elif setting.LEVEL_OF_SCREEN == 4:
            self.menu_pause.draw() # Vẽ menu pause
        elif setting.LEVEL_OF_SCREEN == 5:
            self.board = Board(self.screen)
            self.menu_win.draw() # Vẽ menu win
        elif setting.LEVEL_OF_SCREEN == 6:
            self.board = Board(self.screen)
            self.menu_lose.draw()