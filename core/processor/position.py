from core import config

def get_pixel_position(row, col):
    """Đổi từ vị trí của quân trong board sang vị trí điểm(pixel) tương ứng với trong screen"""
    x = config.BOARD_X + (col - 1) * config.TILE_SIZE + config.TILE_SIZE // 2
    y = config.BOARD_Y + (row - 1) * config.TILE_SIZE + config.TILE_SIZE // 2
    return x, y