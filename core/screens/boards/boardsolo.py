import pygame.time

from assets import assets
from core import button, setting, processor, config
from core.screens.boards.board import Board


class BoardOfSolo(Board):
    pause_time = 0
    start_time = pygame.time.get_ticks()
    hint = 7
    shuffle = 7
    def __init__(self, screen):
        super().__init__(screen)
        # create the shuffle button and the hint button
        self.shuffle = button.btnshuffle.btnShuffle(assets.button_path["shuffle"],
                                                    (config.SCREEN_WIDTH // 2 - 80, 25))
        self.hint = button.btnhint.btnHint(assets.button_path["hint"], (config.SCREEN_WIDTH // 2 + 55, 25))
        # Timer
        BoardOfSolo.start_time = pygame.time.get_ticks()
        BoardOfSolo.pause_time = 0
        self.time_limit = max(200 - (Board.level - 1) * 20, 50)
        self.remaining_time = 0

    def check_any_valid_pair(self):
        if processor.hint.Hint.get_hint(self.tiles) is not None:
            return
        processor.generate.Gennergate.gennerage_board(assets.pokemon_images, self.tiles, self.total_tiles, self.num_tiles_lost)
        BoardOfSolo.shuffle -= 1
        setting.LOSE = BoardOfSolo.shuffle == 0

    def you_lose(self):
        setting.LOSE = self.remaining_time == 0

    def draw(self):
        super().draw()
        font = pygame.font.Font(setting.FONT_PATH, 30)
        # draw the shuffle button and the hint button
        self.hint.draw(self.screen)
        self.shuffle.draw(self.screen)
        hint_text = font.render(f"{BoardOfSolo.hint}", True, config.WHITE)
        shuffle_text = font.render(f"{BoardOfSolo.shuffle}", True, config.WHITE)
        self.screen.blit(hint_text, (config.SCREEN_WIDTH // 2 + 12.5, 10))
        self.screen.blit(shuffle_text, (config.SCREEN_WIDTH // 2 - 55, 10))
        # Draw scope
        score_text = pygame.font.Font(setting.FONT_PATH, 30).render(f"Điểm: {Board.total_score}", True, config.WHITE)
        text_rect = score_text.get_rect(
            center=(config.SCREEN_WIDTH // 2, ((config.NUM_ROWS + 2) * config.TILE_SIZE) + 50))
        self.screen.blit(score_text, text_rect)
        # Timer
        elapsed_time = (pygame.time.get_ticks() - BoardOfSolo.start_time) // 1000
        self.remaining_time = max(self.time_limit - elapsed_time, 0)  # đảm bảo không âm
        # Draw time
        time_text = font.render(f"Time: {self.remaining_time}s - Level: {Board.level}", True, config.WHITE)
        self.screen.blit(time_text, (10, 10))
        self.you_lose()
        pygame.display.flip()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hint.rect.collidepoint(event.pos) and BoardOfSolo.hint > 0:
                print("Bạn đã nhận được sự trợ giúp")
                (r1, c1), (r2, c2) = processor.hint.Hint.get_hint(self.tiles)
                print(f"({r1}, {c1}) - ({r2}, {c2})")
                self.tiles[r1][c1].is_hinted = True
                self.tiles[r2][c2].is_hinted = True
                BoardOfSolo.hint -= 1

            if self.shuffle.rect.collidepoint(event.pos) and BoardOfSolo.shuffle > 0:
                print("Bạn đã chọn đảo")
                processor.generate.Gennergate.gennerage_board(assets.pokemon_images, self.tiles, self.total_tiles, self.num_tiles_lost)
                BoardOfSolo.shuffle -= 1

            for btn in self.restart_back.buttons:
                if btn.btn["rect"].collidepoint(event.pos):
                    BoardOfSolo.shuffle, BoardOfSolo.hint = 7, 7
                    if btn.btn_name == "Restart":
                        BoardOfSolo.start_time = pygame.time.get_ticks()