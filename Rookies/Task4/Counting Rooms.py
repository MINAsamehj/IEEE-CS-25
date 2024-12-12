#### important note
### i runned it on pypy3  
### i dont have any idea what is that pypy , but it runs faster
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

visited = [[False] * m for _ in range(n)]
room_count = 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' and not visited[i][j]:
            stack = [(i, j)]
            visited[i][j] = True
            
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == '.':
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            
            room_count += 1

print(room_count)
