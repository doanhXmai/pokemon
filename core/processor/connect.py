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
        # Kiểm tra 2 ô cùng vị trí
        if pos1 == pos2:
            return None

        r1, c1 = pos1
        r2, c2 = pos2

        # Kiểm tra 2 ô cùng loại (so sánh đường dẫn hình ảnh)
        if tiles[r1][c1].image_path != tiles[r2][c2].image_path:
            return None

        # Tìm đường nối giữa 2 ô
        path = processor.BFS.find_pass(tiles, pos1, pos2)
        # Số ô trong đường nối (bao gồm ô xuất phát và đích) phải từ 2 đến 4
        if 2 <= len(path) <= 4:
            return path
        return None
    @staticmethod
    def draw_connection(screen, path, color = config.RED, width = 5):
        if not path:
            return
        for i in range(len(path) - 1):
            pygame.draw.line(screen, color, processor.position.get_pixel_position(*path[i]), get_pixel_position(*path[i+1]), width)
