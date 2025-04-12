# hoạt động của bot
import pygame.time

from core import setting
from core.processor.hint import Hint


class Bot:
    score = 0
    def __init__(self):
        self.last_action = pygame.time.get_ticks()

    def update(self, tiles):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_action >= setting.DELAY:
            hint = Hint.get_hint(tiles)
            self.last_action = pygame.time.get_ticks()
            if hint:
                (row1, col1), (row2, col2) = hint
                print(f"🤖 Bot nối: ({row1},{col1}) ↔ ({row2},{col2})")
                return hint
        return None