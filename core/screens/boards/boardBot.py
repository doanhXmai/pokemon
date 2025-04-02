from core.screens.boards.board import Board


class BoardBattleBot(Board):
    game_over = False
    def __init__(self, screen):
        super().__init__(screen)