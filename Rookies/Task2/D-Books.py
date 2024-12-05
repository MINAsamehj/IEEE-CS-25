n, t = map(int, input().split())
reading_times = list(map(int, input().split()))

start = 0
current_time = 0
max_books = 0

for end in range(n):
    current_time += reading_times[end]
    while current_time > t:
        current_time -= reading_times[start]
        start += 1
    max_books = max(max_books, end - start + 1)

print(max_books)
