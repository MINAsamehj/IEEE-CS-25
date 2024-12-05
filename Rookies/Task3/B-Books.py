n, t = map(int, input().split())
times = list(map(int, input().split()))

left = 0
max_count = 0




total_time = 0

for right in range(n):
    total_time += times[right]
    while total_time > t:
        total_time -= times[left]
        left += 1
    max_count = max(max_count, right - left + 1)

print(max_count)
