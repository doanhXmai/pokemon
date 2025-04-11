import sys
import pygame

from core import setting, config, screens, sound
from core.screens.menu.menuwin import MenuWin


class Game:
    def __init__(self):
        pygame.init() # Run pygame
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Pokémon Nối hình")

        pygame.display.set_icon(pygame.image.load("assets/images/pieces2.png"))

        # load sounds
        sound.sound.Sound.load_sound()

        # screen menus
        self.menu_start = screens.menu.menustart.MenuStart(self.screen)
        self.menu_level = screens.menu.menulevel.MenuLevel(self.screen)
        self.menu_pause = screens.menu.menupause.MenuPause(self.screen)
        self.menu_win = screens.menu.menuwin.MenuWin(self.screen)
        self.menu_lose = screens.menu.menulose.MenuLose(self.screen)

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
            elif setting.LEVEL_OF_SCREEN == 3:
                self.board.handle_event(event)
            elif setting.LEVEL_OF_SCREEN == 4:
                self.menu_pause.handle_event(event)
            elif setting.LEVEL_OF_SCREEN == 5:
                self.menu_win.handle_event(event)
            elif setting.LEVEL_OF_SCREEN == 6:
                self.menu_lose.handle_event(event)
            elif setting.LEVEL_OF_SCREEN == 7:
                self.board.handle_event(event)

    def draw(self):
        if setting.LEVEL_OF_SCREEN == 0:
            self.menu_start.draw()  # Draw start menu
        elif setting.LEVEL_OF_SCREEN == 1:
            self.menu_level.draw()  # Draw mode selection menu
        elif setting.LEVEL_OF_SCREEN == 2:
            if screens.boards.board.Board.back:
                self.board = None
                screens.boards.board.Board.back = False
            if self.board is None: self.board = screens.boards.boardsolo.BoardOfSolo(self.screen)
            self.board.draw()
            if setting.LOSE:
                sound.sound.Sound.play_music(config.LOSE)
                setting.LEVEL_OF_SCREEN = 6
                setting.LOSE = False
                screens.boards.boardsolo.BoardOfSolo.shuffle = 7
                screens.boards.boardsolo.BoardOfSolo.hint = 7
            if setting.WIN:
                sound.sound.Sound.play_music(config.WIN)
                setting.LEVEL += 1                  # Level up
                setting.SCORE = 10 * setting.LEVEL  # increase score
                setting.LEVEL_OF_SCREEN = 5
                setting.WIN = False
                MenuWin.isSolo = True
        elif setting.LEVEL_OF_SCREEN == 3:
            if screens.boards.board.Board.back:
                self.board = None
                screens.boards.board.Board.back = False
            if self.board is None: self.board = screens.boards.boardBot.BoardBattleBot(self.screen)
            self.board.draw()
        elif setting.LEVEL_OF_SCREEN == 4:
            self.menu_pause.draw()          # Draw the pause menu
        elif setting.LEVEL_OF_SCREEN == 5:
            self.menu_win.draw()            # Draw the win menu
        elif setting.LEVEL_OF_SCREEN == 6:
            self.menu_lose.draw()           # Draw the lose menu
        elif setting.LEVEL_OF_SCREEN == 7:
            if screens.boards.board.Board.back:
                self.board = None
                screens.boards.board.Board.back = False
            if self.board is None: self.board = screens.boards.boardtraning.BoardOfTraining(self.screen)
            self.board.draw()
            if setting.WIN:
                sound.sound.Sound.play_music(config.WIN)
                setting.LEVEL += 1  # Level up
                setting.SCORE = 10 * setting.LEVEL
                setting.LEVEL_OF_SCREEN = 5
                setting.WIN = False
                MenuWin.isSolo = False