n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
count = 0
for row in matrix:
    if sum(row) == 1:
        count += 1
print(count)
