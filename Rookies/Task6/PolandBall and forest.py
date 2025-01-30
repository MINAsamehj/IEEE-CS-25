n = int(input())
p = list(map(int, input().split()))

unique_roots = set()
for i in range(n):
    unique_roots.add(p[i])

print(len(unique_roots))
