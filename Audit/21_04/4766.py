n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]

edges = []
for i in range(n):
    for j in range(n):
        if adj[i][j] == 1:
            edges.append((i + 1, j + 1))

for edge in edges:
    print(*edge)
