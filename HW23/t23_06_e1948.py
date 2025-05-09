n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

queue = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

sorted_order = []

while queue:
    node = queue.pop(0)
    sorted_order.append(node)

    for neighbor in graph[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            queue.append(neighbor)

if len(sorted_order) == n:
    print(*sorted_order)
else:
    print(-1)
