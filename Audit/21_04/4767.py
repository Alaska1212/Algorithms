n, m = map(int, input().split())
adj_matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    adj_matrix[u - 1][v - 1] = 1

for row in adj_matrix:
    print(*row)
