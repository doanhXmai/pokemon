import pygame

from core import config
from core import processor
from core.processor.position import get_pixel_position

class ConnectProcessing:
    @staticmethod
    def can_connect(tiles, pos1, pos2):
        """
        Kiểm tra 2 ô có thể nối với nhau không:
         - 2 ô phải khác vị trí.
         - Phải cùng hình ảnh.
         - Và có đường nối hợp lệ (đường nối có số điểm nằm trong khoảng từ 2 đến 4).
        """
        # Two points in the same location
        if pos1 == pos2:
            return None

        r1, c1 = pos1
        r2, c2 = pos2

        if tiles[r1][c1] is None or tiles[r2][c2] is None: return None

        # Two points must be to the same type (so sánh đường dẫn hình ảnh)
        if tiles[r1][c1].image_path != tiles[r2][c2].image_path:
            return None

        # Find path
        path = processor.BFS.find_pass(tiles, pos1, pos2)
        # The number of cells in the path (including the starting and destination cells) must be from 2 to 4
        if 2 <= len(path) <= 4:
            return path
        return None
    @staticmethod
    def draw_connection(screen, path, color = config.RED, width = 5):
        if not path:
            return
        for i in range(len(path) - 1):
            pygame.draw.line(screen, color, processor.position.get_pixel_position(*path[i]), get_pixel_position(*path[i+1]), width)