n = int(input())
gr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if gr[i][j] == 1:
            print( i+1, j + 1)