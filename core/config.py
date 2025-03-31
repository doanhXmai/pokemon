# Đây là file cấu hình của game

# Số hàng và cột của broad
NUM_COLS = 12
NUM_ROWS = 9

# Kích thước mỗi ô
TILE_SIZE = 48

# Kích thước màn hình hiển thị
SCREEN_WIDTH = NUM_COLS * TILE_SIZE + 400
SCREEN_HEIGHT = NUM_ROWS * TILE_SIZE + 200

# Dùng để xác định vị trí giúp căn giữa
BOARD_X = (SCREEN_WIDTH - NUM_COLS * TILE_SIZE) // 2
BOARD_Y = (SCREEN_HEIGHT - NUM_ROWS * TILE_SIZE) // 2

# Màu sắc
ORANGE = (255, 140, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
RED = (255, 50, 50)
LIME_GREEN = (50, 205, 50)
GREEN = (125, 255, 0)
LIGHT_BLUE = (173, 216, 230)
DODGER_BLUE = (30, 144, 255)
BLUE = (0, 0, 255)
LIGHT_PINK = (255, 182, 193)


# Âm thanh
CLICK = "click"
WIN = "win"
LOSE = "lose"
MATCHED = "matched"
NOT_SELECTED = "notselected"