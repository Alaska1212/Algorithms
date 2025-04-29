n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

sources = []
sinks = []

for i in range(n):
    if sum(adj_matrix[j][i] for j in range(n)) == 0:
        sources.append(i + 1)
    if sum(adj_matrix[i][j] for j in range(n)) == 0:
        sinks.append(i + 1)

print(len(sources), *sources)
print(len(sinks), *sinks)
