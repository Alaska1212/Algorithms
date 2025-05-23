def solve_labyrinth(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]
    dist = [-float('inf')] * (n + 1)
    dist[1] = 0 

    for u, v, w in edges:
        graph[u].append((v, w))
        reverse_graph[v].append(u)

    updated = [False] * (n + 1)

    for i in range(n):
        for u in range(1, n + 1):
            for v, w in graph[u]:
                if dist[u] != -float('inf') and dist[v] < dist[u] + w:
                    dist[v] = dist[u] + w
                    if i == n - 1:
                        updated[v] = True

    reachable = [False] * (n + 1)

    def dfs(v):
        reachable[v] = True
        for u in reverse_graph[v]:
            if not reachable[u]:
                dfs(u)

    dfs(n)

    for v in range(1, n + 1):
        if updated[v] and reachable[v]:
            return ":)"

    if dist[n] == -float('inf'):
        return ":("
    else:
        return dist[n]

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

print(solve_labyrinth(n, m, edges))
