import math
import sys

def prim(points):
    n = len(points)
    used = [False] * n
    min_edge = [float('inf')] * n
    min_edge[0] = 0
    total = 0.0

    for _ in range(n):
        u = -1
        for i in range(n):
            if not used[i] and (u == -1 or min_edge[i] < min_edge[u]):
                u = i

        used[u] = True
        total += min_edge[u]

        for v in range(n):
            if not used[v]:
                dist = math.dist(points[u], points[v])
                if dist < min_edge[v]:
                    min_edge[v] = dist

    return total

def main():
    input_data = sys.stdin.read().splitlines()
    i = 0
    while i < len(input_data):
        line = input_data[i]
        if line == '0':
            break
        n = int(line)
        i += 1
        points = []
        for _ in range(n):
            x, y = map(int, input_data[i].split())
            points.append((x, y))
            i += 1
        result = prim(points)
        print(f"{result:.2f}")

if __name__ == "__main__":
    main()
