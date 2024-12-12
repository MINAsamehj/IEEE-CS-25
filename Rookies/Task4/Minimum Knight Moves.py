from collections import deque

start, last = input().split()

def fixing_points(position):
    position = position.lower()
    col = ord(position[0]) - ord('a')
    row = int(position[1]) - 1
    return col, row

start = fixing_points(start)
last = fixing_points(last)

possible_moves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

queue = deque([(start[0], start[1], 0)])
visited = set()
visited.add(start)

while queue:
    x, y, steps = queue.popleft()
    
    if (x, y) == last:
        print(steps) 
        break

    for dx, dy in possible_moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny) and (nx, ny) not in visited:
            visited.add((nx, ny))
            queue.append((nx, ny, steps + 1))
