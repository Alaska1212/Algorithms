n, k, a, b, d = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(k):
    u, v = map(int, input().split())
    graph[u].append(v)
count = 0

def dfs(u, depth, visited):
    global count
    if depth > d:
        return
    if u == b:
        count += 1
        return
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v, depth + 1, visited)
            visited[v] = False

visited = [False] * (n + 1)
visited[a] = True
dfs(a, 0, visited)

print(count)
