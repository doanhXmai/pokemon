from collections import deque


def find_pass(tiles, pos1, pos2):
    """
        Tìm đường nối giữa pos1 và pos2 (theo dạng (row, col)) bằng thuật toán BFS.
        Tạo ma trận grid từ self.tiles với viền rỗng. Các ô có giá trị None được coi là trống.
        Các ô chứa Tile được xem là chướng ngại vật, ngoại trừ 2 ô được chọn.
    """
    R = len(tiles)
    C = len(tiles[0])
    # create a grid, 0: empty, 1: has tile
    grid = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if tiles[r][c] is not None:
                grid[r][c] = 1

    # Get the coordinates of the 2 cells to be joined
    r1, c1 = pos1
    r2, c2 = pos2

    # Allows passing through the origin and destination cells (even though they have tiles)
    grid[r1][c1] = 0
    grid[r2][c2] = 0

    # Initialize trace to save path
    trace = [[None for _ in range(C)] for _ in range(R)]
    q = deque()
    q.append(pos2)
    trace[r2][c2] = (-2, -2)  # Mark the origin of the trace

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        cur = q.popleft()
        if cur == pos1:
            break
        for dx, dy in directions:
            nr = cur[0] + dx
            nc = cur[1] + dy
            # Toward one direction continuously until you encounter an obstacle.
            while 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                # R > nr >= 0 == grid[nr][nc] and 0 <= nc < C
                if trace[nr][nc] is None:
                    trace[nr][nc] = cur
                    q.append((nr, nc))
                nr += dx
                nc += dy

    # If having a path, it would trace the path
    return trace_path(trace, pos1)

def trace_path(trace, pos):
    path = []
    if trace[pos[0]][pos[1]] is not None:
        cur = pos
        while cur != (-2, -2):
            # Note: coordinates here are according to the coordinates of self.tiles (had a border)
            path.append(cur)
            cur = trace[cur[0]][cur[1]]
        path.reverse()  # Need path from pos2 to pos1, can be reverse
    return path