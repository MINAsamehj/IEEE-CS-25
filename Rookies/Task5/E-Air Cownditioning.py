def min_cost(idx, cooling, cost):
    if idx == len(ac_units):
        for i in range(101):
            if cooling[i] < cow_requirements[i]:
                return float('inf')
        return cost
    a, b, p, m = ac_units[idx]
    new_cooling = cooling[:]
    for i in range(a, b + 1):
        new_cooling[i] += p
    return min(min_cost(idx + 1, cooling, cost), min_cost(idx + 1, new_cooling, cost + m))

n, m = map(int, input().split())
cow_requirements = [0] * 101
for _ in range(n):
    s, t, c = map(int, input().split())
    for i in range(s, t + 1):
        cow_requirements[i] = c

ac_units = []
for _ in range(m):
    a, b, p, m = map(int, input().split())
    ac_units.append((a, b, p, m))

print(min_cost(0, [0] * 101, 0))
