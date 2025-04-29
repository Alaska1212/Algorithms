N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
degrees = [0] * N
for i in range(N):
    degrees[i] = sum(adj[i])
print(*degrees)
