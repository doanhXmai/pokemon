from collections import deque


def find_pass(tiles, pos1, pos2):
    """
        Tìm đường nối giữa pos1 và pos2 (theo dạng (row, col)) bằng thuật toán BFS.
        Tạo ma trận grid từ self.tiles với viền rỗng. Các ô có giá trị None được coi là trống.
        Các ô chứa Tile được xem là chướng ngại vật, ngoại trừ 2 ô được chọn.
    """
    R = len(tiles)
    C = len(tiles[0])
    # Tạo grid, 0: ô trống, 1: có tile
    grid = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if tiles[r][c] is not None:
                grid[r][c] = 1

    # Lấy tọa độ của 2 ô cần nối
    r1, c1 = pos1
    r2, c2 = pos2

    # Cho phép đi qua ô ban đầu và ô đích (mặc dù chúng có tile)
    grid[r1][c1] = 0
    grid[r2][c2] = 0

    # Khởi tạo trace để lưu lại đường đi
    trace = [[None for _ in range(C)] for _ in range(R)]
    q = deque()
    q.append(pos2)
    trace[r2][c2] = (-2, -2)  # Đánh dấu điểm gốc của trace

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while q:
        cur = q.popleft()
        if cur == pos1:
            break
        for dx, dy in directions:
            nr = cur[0] + dx
            nc = cur[1] + dy
            # Di chuyển theo 1 hướng liên tục cho đến khi gặp chướng ngại
            while 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                if trace[nr][nc] is None:
                    trace[nr][nc] = cur
                    q.append((nr, nc))
                nr += dx
                nc += dy

    # Truy vết lại đường đi nếu có
    return trace_path(trace, pos1)

def trace_path(trace, pos):
    path = []
    if trace[pos[0]][pos[1]] is not None:
        cur = pos
        while cur != (-2, -2):
            # Lưu ý: các tọa độ ở đây vẫn theo hệ thống của self.tiles (đã có viền)
            path.append(cur)
            cur = trace[cur[0]][cur[1]]
        path.reverse()  # Nếu cần đường đi từ pos2 đến pos1, có thể đảo ngược lại
    return path