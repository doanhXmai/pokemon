import pygame.font

import assets.assets
from bot.core.bot import Bot
from core import setting, config, processor, sound
from core.playerHUD.avatarscore import AvatarScore
from core.screens.boards.board import Board


class BoardBattleBot(Board):
    game_over = False
    def __init__(self, screen):
        super().__init__(screen)
        self.bot_action = Bot()
        self.font = pygame.font.Font(setting.FONT_PATH, 24)
        self.player = AvatarScore(assets.assets.avatar_path, (self.board_center_x - 290, self.board_y - 40), Board.total_score, self.font)
        self.bot = AvatarScore(assets.assets.avatar_path, (self.board_center_x + 100, self.board_y - 40), Bot.score, self.font, "bot")


    def draw(self):
        super().draw()
        self.player.draw(self.screen)
        self.player.update_score(Board.total_score)

        self.bot.draw(self.screen)
        self.bot.update_score(Bot.score)

    def handle_event(self, event):
        action_of_bot = self.bot_action.update(self.tiles)
        if action_of_bot:
            path = processor.connect.ConnectProcessing.can_connect(self.tiles, action_of_bot[0], action_of_bot[1])
            processor.connect.ConnectProcessing.draw_connection(self.screen, path)
            pygame.display.update()
            pygame.time.delay(100)
            self.remove_pokemon(action_of_bot[0], action_of_bot[1])
            Bot.score += Board.score
            BoardBattleBot.game_over = self.is_board_empty()

        if event.type == pygame.MOUSEBUTTONDOWN:  # Turn on or turn off volume
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
                    Bot.score = 0
                    self.num_tiles_lost = 0
                    BoardBattleBot.game_over = False

                    if btn.btn_name == "Back":
                        setting.LEVEL_OF_SCREEN = 1
                        Board.back = True
                    elif btn.btn_name == "Restart":
                        processor.generate.Gennergate.gennerage_board(assets.assets.pokemon_images, self.tiles, self.total_tiles)
            for row in range(1, config.NUM_ROWS + 1):
                for col in range(1, config.NUM_COLS + 1):
                    if self.tiles[row][col] is not None and self.tiles[row][col].rect.collidepoint(event.pos):
                        print(f"Bạn đã chọn vị trí: ({row-1}, {col-1}) với {self.tiles[row][col].image_path}")
                        self.tiles[row][col].is_selected = not self.tiles[row][col].is_selected

                        if self.first_tile is None:
                            sound.sound.Sound.play_music(config.CLICK)
                            self.first_tile = (row, col)
                        else:
                            second_tile = (row, col)
                            path = processor.connect.ConnectProcessing.can_connect(self.tiles, self.first_tile, second_tile)

                            if path is not None:
                                print("Nối thành công")
                                self.remove_pokemon((self.first_tile[0], self.first_tile[1]), (second_tile[0], second_tile[1]))
                                BoardBattleBot.game_over = self.is_board_empty()
                                Board.total_score += Board.score
                                print(BoardBattleBot.game_over)
                                self.num_tiles_lost += 2
                                self.check_any_valid_pair()
                                sound.sound.Sound.play_music(config.MATCHED)
                                processor.connect.ConnectProcessing.draw_connection(self.screen, path)
                                pygame.display.update()
                                pygame.time.delay(100)
                            else:
                                print("Nối không thành công")
                                if self.tiles[self.first_tile[0]][self.first_tile[1]] is not None:
                                    self.tiles[self.first_tile[0]][self.first_tile[1]].is_selected = False
                                if self.tiles[second_tile[0]][second_tile[1]] is not None:
                                    self.tiles[second_tile[0]][second_tile[1]].is_selected = False
                                sound.sound.Sound.play_music(config.NOT_SELECTED)
                            self.first_tile = None

