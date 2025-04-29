n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

adj_matrix = [[0] * n for _ in range(n)]

for u, v in edges:
    adj_matrix[u - 1][v - 1] = 1

for i in range(n):
    for j in range(n):
        if i != j and adj_matrix[i][j] + adj_matrix[j][i] != 1:
            print("NO")
            exit()

print("YES")
