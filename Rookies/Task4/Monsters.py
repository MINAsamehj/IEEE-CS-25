####there is runtime error in one test because its a python file 


from collections import deque

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIRS = ['R', 'L', 'D', 'U']

def bfs(n, m, grid, start):
    player_queue = deque([start])
    monster_queue = deque()
    visited_player = [[False] * m for _ in range(n)]
    visited_monster = [[False] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]

    sx, sy = start
    visited_player[sx][sy] = True

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'M':
                monster_queue.append((i, j))
                visited_monster[i][j] = True

    while player_queue:
        x, y = player_queue.popleft()

        if x == 0 or x == n-1 or y == 0 or y == m-1:
            path = []
            while parent[x][y] is not None:
                px, py, dir_idx = parent[x][y]
                path.append(DIRS[dir_idx])
                x, y = px, py
            return True, ''.join(path[::-1])

        for i, (dx, dy) in enumerate(DIRECTIONS):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited_player[nx][ny] and grid[nx][ny] != '#':
                if not visited_monster[nx][ny]:
                    visited_player[nx][ny] = True
                    parent[nx][ny] = (x, y, i)
                    player_queue.append((nx, ny))
        
        size = len(monster_queue)
        for _ in range(size):
            mx, my = monster_queue.popleft()
            for dx, dy in DIRECTIONS:
                nm_x, nm_y = mx + dx, my + dy
                if 0 <= nm_x < n and 0 <= nm_y < m and not visited_monster[nm_x][nm_y] and grid[nm_x][nm_y] != '#':
                    visited_monster[nm_x][nm_y] = True
                    monster_queue.append((nm_x, nm_y))

    return False, ""

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

start = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'A':
            start = (i, j)
            break
    if start:
        break

possible, path = bfs(n, m, grid, start)

if possible:
    print("YES")
    print(len(path))
    print(path)
else:
    print("NO")
