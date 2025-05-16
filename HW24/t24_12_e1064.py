from collections import deque

def knight_path(n, board):
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    starts = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == '@':
                starts.append((i, j))

    if len(starts) != 2:
        return "Impossible"

    start, end = starts
    visited = [[False]*n for _ in range(n)]
    prev = [[None]*n for _ in range(n)]

    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    found = False
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            found = True
            break
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and board[nx][ny] != '#':
                    visited[nx][ny] = True
                    prev[nx][ny] = (x, y)
                    queue.append((nx, ny))

    if not found:
        return "Impossible"

    # Відновлення шляху
    x, y = end
    while (x, y) != start:
        if board[x][y] == '.':
            board[x][y] = '@'
        x, y = prev[x][y]

    return [''.join(row) for row in board]

def main():
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    result = knight_path(n, board)
    if result == "Impossible":
        print("Impossible")
    else:
        for row in result:
            print(row)

if __name__ == "__main__":
    main()
