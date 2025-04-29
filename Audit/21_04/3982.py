n = int(input())
gr = [[0] * n for _ in range(n)]

for i in range(n):
    parts = list(map(int, input().split()))
    k = parts[0]
    for j in range(1, k + 1):
        vert = parts[j] - 1
        gr[i][vert] = 1

for row in gr:
    print(' '.join(map(str, row)))