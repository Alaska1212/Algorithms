def bfs(lab, start, end, n, m):
    visited = [[False] * m for _ in range(n)]
    dist = [[-1] * m for _ in range(n)]
    queue = [start]
    visited[start[0]][start[1]] = True
    dist[start[0]][start[1]] = 0

    while queue:
        x, y = queue.pop(0)

        if (x, y) == end:
            return dist[x][y]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and lab[nx][ny] == 0:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return -1

def main():
    N, M = map(int, input().split())
    lab = []
    for _ in range(N):
        lab.append(list(map(int, input().split())))

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    start = (y1 - 1, x1 - 1)
    end = (y2 - 1, x2 - 1)

    result = bfs(lab, start, end, N, M)
    print(result)

if __name__ == "__main__":
    main()
