import heapq

def prim(n, graph):
    visited = [False] * (n + 1)
    min_heap = [(0, 1)]
    total_weight = 0
    count = 0

    while min_heap and count < n:
        heapq.heapify(min_heap)
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        count += 1
        new_edges = []
        for v, w in graph[u]:
            if not visited[v]:
                new_edges.append((w, v))
        min_heap.extend(new_edges)

    return total_weight

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(prim(n, graph))