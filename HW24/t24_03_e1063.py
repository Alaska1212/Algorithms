def dfs(x, y, grid, visited, m, n):
    stack = [(x, y)]
    while stack:
        i, j = stack.pop()
        if visited[i][j]:
            continue
        visited[i][j] = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n:
                if grid[ni][nj] == '#' and not visited[ni][nj]:
                    stack.append((ni, nj))

def main():
    m, n = map(int, input().split())
    grid = [list(input().strip()) for _ in range(m)]
    visited = [[False]*n for _ in range(m)]
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#' and not visited[i][j]:
                dfs(i, j, grid, visited, m, n)
                count += 1

    print(count)

if __name__ == "__main__":
    main()
