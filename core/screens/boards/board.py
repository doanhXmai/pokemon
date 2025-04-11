import pygame

from assets import assets
from core import setting, config, button, processor, screens, sound
from core.screens.screen import Screen

class Board(Screen):

    score = 10
    back = False
    total_score = 0
    level = 1

    def __init__(self, screen):
        super().__init__(screen)
        self.total_tiles = config.NUM_ROWS * config.NUM_COLS
        self.num_tiles_lost = 0

        # The board has a size of (NUM_ROWS+2) x (NUM_COLS+2) to add a empty border
        self.tiles = [[None for _ in range(config.NUM_COLS + 2)] for _ in range(config.NUM_ROWS + 2)]
        self.first_tile = None

        # Create Board
        processor.generate.Gennergate.gennerage_board(assets.pokemon_images, self.tiles, self.total_tiles)

        # Create buttons
        self.board_center_x = config.SCREEN_WIDTH // 2
        self.board_y = config.BOARD_Y - 40

        self.pause = button.btnpause.btnPause(assets.button_path["pause"], (self.board_center_x, self.board_y))
        self.restart_back = button.btnrestartandback.btnRestartAndBack()

    def is_board_empty(self):
        """Confirm that the board tiles are None"""
        for row in self.tiles:
            for col in row:
                if col is not None:
                    return False
        return True

    def remove_pokemon(self, pop1, pop2):
        self.tiles[pop1[0]][pop1[1]] = None
        self.tiles[pop2[0]][pop2[1]] = None

    def check_any_valid_pair(self):
        """There are no more pairs of Pokémon"""
        if processor.hint.Hint.get_hint(self.tiles) is not None:
            return
        processor.generate.Gennergate.gennerage_board(assets.pokemon_images, self.tiles, self.total_tiles, self.num_tiles_lost)

    def draw(self):
        self.screen.blit(screens.background.Background.load_image(assets.background), (0, 0))

        for row in range(1, config.NUM_ROWS + 1):
            for col in range(1, config.NUM_COLS + 1):
                if self.tiles[row][col] is not None:
                    self.tiles[row][col].draw(self.screen) # Draw each tile

        # Draw button
        self.draw_sound_button()
        self.pause.draw(self.screen)
        self.restart_back.draw(self.screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: # Turn on or turn off volume
            if self.sound_rect.collidepoint(event.pos):
                self.toggle_sound()

            if self.pause.rect.collidepoint(event.pos):
                print("Bạn đã tạm dừng")
                sound.sound.Sound.play_music(config.CLICK)
                if not setting.PAUSE:
                    setting.LEVEL_OF_SCREEN = 4
                    setting.PAUSE = True
                    Board.pause_time = pygame.time.get_ticks()

            for btn in self.restart_back.buttons:
                if btn.btn["rect"].collidepoint(event.pos):
                    print(f"Bạn đã chọn vào {btn.btn_name}")
                    sound.sound.Sound.play_music(config.CLICK)
                    Board.total_score = 0
                    Board.level = 1
                    self.num_tiles_lost = 0

                    if btn.btn_name == "Back":
                        setting.LEVEL_OF_SCREEN = 1
                        Board.back = True
                    elif btn.btn_name == "Restart":
                        processor.generate.Gennergate.gennerage_board(assets.pokemon_images, self.tiles, self.total_tiles)

            for row in range(1, config.NUM_ROWS + 1):
                for col in range(1, config.NUM_COLS + 1):
                    if self.tiles[row][col] is not None and self.tiles[row][col].rect.collidepoint(event.pos):
                        print(f"Bạn đã chọn vị trí: ({row-1}, {col-1}) với {self.tiles[row][col].image_path}")
                        self.tiles[row][col].is_selected = not self.tiles[row][col].is_selected

                        if not self.first_tile:
                            sound.sound.Sound.play_music(config.CLICK)
                            self.first_tile = (row, col)
                        else:
                            second_tile = (row, col)
                            path = processor.connect.ConnectProcessing.can_connect(self.tiles, self.first_tile, second_tile)

                            if path is not None:
                                print("Nối thành công")
                                self.remove_pokemon((self.first_tile[0], self.first_tile[1]), (second_tile[0], second_tile[1]))
                                setting.WIN = self.is_board_empty()
                                Board.total_score += Board.score
                                self.num_tiles_lost += 2
                                self.check_any_valid_pair()
                                sound.sound.Sound.play_music(config.MATCHED)
                                processor.connect.ConnectProcessing.draw_connection(self.screen, path)
                                pygame.display.update()
                                pygame.time.delay(300)
                            else:
                                print("Nối không thành công")
                                self.tiles[self.first_tile[0]][self.first_tile[1]].is_selected = False
                                self.tiles[second_tile[0]][second_tile[1]].is_selected = False
                                sound.sound.Sound.play_music(config.NOT_SELECTED)
                            self.first_tile = None
