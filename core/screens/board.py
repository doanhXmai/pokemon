import pygame

from core import setting, config, button, processor, screens, sound
from core.screens.screen import Screen

class Board(Screen):

    back = False
    pokemon_images = [f"assets/images/pieces{i}.png" for i in range(1, 20)]
    pause_time = 0
    start_time = pygame.time.get_ticks()

    def __init__(self, screen):
        super().__init__(screen)
        self.total_tiles = config.NUM_ROWS * config.NUM_COLS
        self.num_tiles_lost = 0

        Board.start_time = pygame.time.get_ticks()
        Board.pause_time = 0

        # The board has a size of (NUM_ROWS+2) x (NUM_COLS+2) to add a empty border
        self.tiles = [[None for _ in range(config.NUM_COLS + 2)] for _ in range(config.NUM_ROWS + 2)]
        self.first_tile = None

        # Create buttons
        board_center_x = config.SCREEN_WIDTH // 2
        board_y = config.BOARD_Y - 40

        self.pause = button.btnpause.btnPause("assets/images/pause.png", (board_center_x, board_y))
        self.hint = button.btnhint.btnHint("assets/images/hint.png", (board_center_x + 50, board_y))
        self.shuffle = button.btnshuffle.btnShuffle("assets/images/shuffle.png", (board_center_x + 100, board_y))
        self.restart_back = button.btnrestartandback.btnRestartAndBack()

        # Create Board
        processor.generate.Gennergate.gennerage_board(Board.pokemon_images, self.tiles, self.total_tiles)
        # Bộ đếm thời gian
        self.time_limit = max(200 - (setting.LEVEL - 1) * 20, 10)
        print(f"time được cập nhật: {self.time_limit}")
        self.remaining_time = 0

    def is_board_empty(self):
        """Confirm that the board tiles are None"""
        for row in self.tiles:
            for col in row:
                if col is not None:
                    return False
        return True

    def check_any_valid_pair(self):
        """There are no more pairs of Pokémon"""
        if processor.hint.Hint.get_hint(self.tiles) is not None:
            return
        processor.generate.Gennergate.gennerage_board(Board.pokemon_images, self.tiles, self.total_tiles, self.num_tiles_lost)

    def you_lose(self):
        setting.LOSE = self.remaining_time == 0

    def draw(self):
        self.screen.blit(screens.background.Background.load_image("assets/images/bgk.jpg"), (0, 0))

        for row in range(1, config.NUM_ROWS + 1):
            for col in range(1, config.NUM_COLS + 1):
                if self.tiles[row][col] is not None:
                    self.tiles[row][col].draw(self.screen) # Draw each tile

        # Draw scope
        score_text = pygame.font.Font(setting.FONT_PATH, 36).render(f"Điểm: {setting.TOTAL_SCORE}", True, (0, 0, 0))
        text_rect = score_text.get_rect(center=(config.SCREEN_WIDTH // 2, ((config.NUM_ROWS + 2) * config.TILE_SIZE) + 50))
        self.screen.blit(score_text, text_rect)

        # Draw button
        self.draw_sound_button()
        self.pause.draw(self.screen)
        self.hint.draw(self.screen)
        self.shuffle.draw(self.screen)
        self.restart_back.draw(self.screen)

        # Timer
        elapsed_time = (pygame.time.get_ticks() - Board.start_time) // 1000
        self.remaining_time = max(self.time_limit - elapsed_time, 0)  # đảm bảo không âm
        # Draw time
        font = pygame.font.Font(setting.FONT_PATH, 50)
        time_text = font.render(f"Time: {self.remaining_time}s - Level: {setting.LEVEL}", True, config.BLACK)
        self.screen.blit(time_text, (10, 10))
        self.you_lose()
        pygame.display.flip()

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

            if self.hint.rect.collidepoint(event.pos):
                print("Bạn đã nhận được sự trợ giúp")
                (r1, c1), (r2, c2) = processor.hint.Hint.get_hint(self.tiles)
                print(f"({r1}, {c1}) - ({r2}, {c2})")
                self.tiles[r1][c1].is_hinted = True
                self.tiles[r2][c2].is_hinted = True

            if self.shuffle.rect.collidepoint(event.pos):
                print("Bạn đã chọn đảo")
                processor.generate.Gennergate.gennerage_board(Board.pokemon_images, self.tiles, self.total_tiles, self.num_tiles_lost)

            for btn in self.restart_back.buttons:
                if btn.btn["rect"].collidepoint(event.pos):
                    print(f"Bạn đã chọn vào {btn.btn_name}")
                    sound.sound.Sound.play_music(config.CLICK)
                    setting.TOTAL_SCORE = 0
                    setting.LEVEL = 1
                    self.num_tiles_lost = 0

                    if btn.btn_name == "Back":
                        setting.LEVEL_OF_SCREEN = 1
                        Board.back = True
                    elif btn.btn_name == "Restart":
                        processor.generate.Gennergate.gennerage_board(Board.pokemon_images, self.tiles, self.total_tiles)
                        Board.start_time = pygame.time.get_ticks()

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
                                self.tiles[self.first_tile[0]][self.first_tile[1]] = None
                                self.tiles[second_tile[0]][second_tile[1]] = None
                                setting.WIN = self.is_board_empty()
                                setting.TOTAL_SCORE += setting.SCORE
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

class BoardOfTrainingMode(Board):
    def __init__(self, screen):
        super().__init__(screen)
class BoardOfBattleBot(Board):
    def __init__(self, screen):
        super().__init__(screen)