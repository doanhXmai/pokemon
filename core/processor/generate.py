import random

from core import config, button


class Gennergate:
    @staticmethod
    def gennerage_board(pokemon_images, tiles, total_tiles, tiles_lost = 0):
        # Tạo bảng với cặp Pokémon và xáo trộn sau khi hoàn tất.
        num_tiles = total_tiles - tiles_lost  # Tổng số ô trên bảng

        if num_tiles % 2 != 0:
            raise ValueError("Số ô trên bảng phải là số chẵn!")

        num_pairs = num_tiles // 2

        # Lặp lại danh sách nếu chưa đủ số cặp cần thiết
        while len(pokemon_images) < num_pairs:
            pokemon_images *= 2

        selected_pokemons = random.sample(pokemon_images, num_pairs)
        tile_pairs = selected_pokemons * 2

        random.shuffle(tile_pairs)

        if tiles_lost == 0:
            Gennergate.plate_pokemon_on_board(tiles, tile_pairs)
        else:
            Gennergate.reset_board_tiles(tiles, tile_pairs)
        return tiles

    @staticmethod
    def plate_pokemon_on_board(tiles, tile_pairs):
        index = 0
        # Ghi chú: các ô trên board được lưu từ index 1 đến NUM_ROWS/NUM_COLS, viền ngoài giữ giá trị None
        for row in range(1, config.NUM_ROWS + 1):
            for col in range(1, config.NUM_COLS + 1):
                x = config.BOARD_X + (col - 1) * config.TILE_SIZE
                y = config.BOARD_Y + (row - 1) * config.TILE_SIZE
                tiles[row][col] = button.tile.Tile(tile_pairs[index], (x, y), (config.TILE_SIZE, config.TILE_SIZE))
                index += 1
    @staticmethod
    def reset_board_tiles(tiles, tile_pairs):
        index = 0
        # Ghi chú: các ô trên board được lưu từ index 1 đến NUM_ROWS/NUM_COLS, viền ngoài giữ giá trị None
        for row in range(1, config.NUM_ROWS + 1):
            for col in range(1, config.NUM_COLS + 1):
                if tiles[row][col] is not None:
                    x = config.BOARD_X + (col - 1) * config.TILE_SIZE
                    y = config.BOARD_Y + (row - 1) * config.TILE_SIZE
                    tiles[row][col] = button.tile.Tile(tile_pairs[index], (x, y), (config.TILE_SIZE, config.TILE_SIZE))
                    index += 1