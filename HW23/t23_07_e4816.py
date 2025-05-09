n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

components = []

def dfs(node, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, component)

for i in range(1, n + 1):
    if not visited[i]:
        component = []
        dfs(i, component)
        components.append(component)

print(len(components))
for component in components:
    print(len(component))
    print(*component)
