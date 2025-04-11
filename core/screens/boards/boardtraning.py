import pygame

from assets import assets
from core import setting, config, button, processor
from core.screens.boards.board import Board


class BoardOfTraining(Board):
    def __init__(self, screen):
        super().__init__(screen)
        # create the shuffle button and the hint button
        self.shuffle = button.btnshuffle.btnShuffle(assets.button_path["shuffle"],
                                                    (self.board_center_x + 100, self.board_y))
        self.hint = button.btnhint.btnHint(assets.button_path["hint"], (self.board_center_x + 50, self.board_y))

    def draw(self):
        super().draw()
        font = pygame.font.Font(setting.FONT_PATH, 50)
        level_text = font.render(f"Level: {setting.LEVEL}", True, config.BLACK)
        self.screen.blit(level_text, (10, 10))

        # draw the shuffle button and the hint button
        self.hint.draw(self.screen)
        self.shuffle.draw(self.screen)

        # Draw scope
        score_text = pygame.font.Font(setting.FONT_PATH, 36).render(f"Điểm: {setting.TOTAL_SCORE}", True, (0, 0, 0))
        text_rect = score_text.get_rect(
            center=(config.SCREEN_WIDTH // 2, ((config.NUM_ROWS + 2) * config.TILE_SIZE) + 50))
        self.screen.blit(score_text, text_rect)

        pygame.display.flip()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hint.rect.collidepoint(event.pos):
                print("Bạn đã nhận được sự trợ giúp")
                (r1, c1), (r2, c2) = processor.hint.Hint.get_hint(self.tiles)
                print(f"({r1}, {c1}) - ({r2}, {c2})")
                self.tiles[r1][c1].is_hinted = True
                self.tiles[r2][c2].is_hinted = True

            if self.shuffle.rect.collidepoint(event.pos):
                print("Bạn đã chọn đảo")
                processor.generate.Gennergate.gennerage_board(assets.pokemon_images, self.tiles, self.total_tiles, self.num_tiles_lost)