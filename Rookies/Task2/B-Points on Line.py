n, d = map(int, input().split())
x = list(map(int, input().split()))

count = 0
r = 0

for l in range(n):
    while r < n and x[r] - x[l] <= d:
        r += 1
    points_in_range = r - l - 1
    if points_in_range >= 2:
        count += points_in_range * (points_in_range - 1) // 2

print(count)
