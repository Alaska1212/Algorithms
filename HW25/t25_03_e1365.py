def dijkstra(n, s, f, matrix):
    INF = float('inf')
    dist = [INF] * n
    used = [False] * n
    dist[s] = 0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not used[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == INF:
            break
        used[u] = True

        for v in range(n):
            if matrix[u][v] != -1 and dist[v] > dist[u] + matrix[u][v]:
                dist[v] = dist[u] + matrix[u][v]

    return dist[f] if dist[f] != INF else -1

n, s, f = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

s -= 1
f -= 1
print(dijkstra(n, s, f, matrix))
