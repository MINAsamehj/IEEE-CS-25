n = int(input())  
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

def dfs(node, graph, visited, current_cost):
    is_leaf = True
    max_cost = current_cost

    for neighbor, cost in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            is_leaf = False
            max_cost = max(max_cost, dfs(neighbor, graph, visited, current_cost + cost))
            visited[neighbor] = False

    return current_cost if is_leaf else max_cost

def solve(n, edges):
    graph = {i: [] for i in range(n)}
    for u, v, c in edges:
        graph[u].append((v, c))
        graph[v].append((u, c))

    visited = [False] * n
    visited[0] = True
    return dfs(0, graph, visited, 0)

print(solve(n, edges))
