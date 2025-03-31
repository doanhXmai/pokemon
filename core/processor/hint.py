from core import config, processor

class Hint:
    @staticmethod
    def get_hint(tiles):
        """Hàm gợi ý"""
        for row1 in range(config.NUM_ROWS + 2):
            for col1 in range(config.NUM_COLS + 2):
                tile1 = tiles[row1][col1]
                if tile1 is None:
                    continue
                for row2 in range(config.NUM_ROWS + 2):
                    for col2 in range(config.NUM_COLS + 2):
                        if row1 == row2 and col1 == col2:
                            continue
                        tile2 = tiles[row2][col2]
                        if tile2 is None:
                            continue
                        if processor.connect.ConnectProcessing.can_connect(tiles, (row1, col1), (row2, col2)):
                            return (row1, col1), (row2, col2)
        return None