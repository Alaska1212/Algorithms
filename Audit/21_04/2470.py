n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if adj_matrix[i][i] != 0:
        print("NO")
        exit()

for i in range(n):
    for j in range(i + 1, n):
        if adj_matrix[i][j] != adj_matrix[j][i]:
            print("NO")
            exit()

print("YES")
