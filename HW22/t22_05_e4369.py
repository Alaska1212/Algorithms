n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

k = int(input())
starts = list(map(int, input().split()))

dist = [-1] * (n + 1)
queue = []

for s in starts:
    dist[s] = 0
    queue.append(s)

i = 0
while i < len(queue):
    u = queue[i]
    i += 1
    for v in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            queue.append(v)

max_time = max(dist[1:])
candidates = [i for i, t in enumerate(dist) if t == max_time]
last_vertex = min(candidates)

print(max_time)
print(last_vertex)
