import sys
import pygame

from core import setting, config
from core.config import *
from core.screens.board import Board
from core.screens.menu.menulevel import MenuLevel
from core.screens.menu.menulose import MenuLose
from core.screens.menu.menupause import MenuPause
from core.screens.menu.menustart import MenuStart
from core.screens.menu.menuwin import MenuWin
from core.sound.sound import Sound


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokémon Nối hình")
        Sound.load_sound()

        # Các màn hình menu
        self.menu_start = MenuStart(self.screen)
        self.menu_level = MenuLevel(self.screen)
        self.menu_pause = MenuPause(self.screen)
        self.menu_win = MenuWin(self.screen)
        self.menu_lose = MenuLose(self.screen)

        # Màn hình chơi chính
        self.board = None
        self.running = True

    def run(self):
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
        if not setting.TURN_ON_VOLUME:
            Sound.stop_sound()
        if setting.LEVEL_OF_SCREEN == 0:
            self.menu_start.draw()  # Vẽ menu start
        elif setting.LEVEL_OF_SCREEN == 1:
            self.menu_level.draw()  # Vẽ menu level
            self.board = Board(self.screen)
        elif setting.LEVEL_OF_SCREEN == 2:
            self.board.draw()
            if setting.LOSE:
                Sound.sound_manager.play_sound(config.LOSE)
                setting.LEVEL_OF_SCREEN = 6
                setting.LOSE = False
            if setting.WIN:
                setting.LEVEL += 1  # Chuyển sang level tiếp theo
                setting.SCORE = 10 * setting.LEVEL
                setting.LEVEL_OF_SCREEN = 5
                Sound.sound_manager.play_sound(config.WIN)
                setting.WIN = False
        elif setting.LEVEL_OF_SCREEN == 4:
            self.menu_pause.draw() # Vẽ menu pause
        elif setting.LEVEL_OF_SCREEN == 5:
            self.board = Board(self.screen)
            self.menu_win.draw() # Vẽ menu win
        elif setting.LEVEL_OF_SCREEN == 6:
            self.board = Board(self.screen)
            self.menu_lose.draw()