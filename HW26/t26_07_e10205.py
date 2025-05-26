import math
import sys

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def solve_prim_no_heap(n, coords, existing):
    INF = float('inf')
    in_mst = [False] * (n + 1)
    key = [INF] * (n + 1)
    parent = [-1] * (n + 1)
    adj = [[None] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                adj[i][j] = distance(coords[i], coords[j])
    for u, v in existing:
        adj[u][v] = 0
        adj[v][u] = 0
    key[1] = 0
    for _ in range(1, n + 1):
        u = -1
        min_key = INF
        for v in range(1, n + 1):
            if not in_mst[v] and key[v] < min_key:
                min_key = key[v]
                u = v
        if u == -1:
            break
        in_mst[u] = True
        for v in range(1, n + 1):
            if not in_mst[v] and adj[u][v] is not None and adj[u][v] < key[v]:
                key[v] = adj[u][v]
                parent[v] = u
    new_highways = []
    for v in range(2, n + 1):
        u = parent[v]
        if u != -1 and adj[u][v] != 0:
            new_highways.append((u, v))
    return new_highways

def parse_input(input_lines):
    i = 0
    T = int(input_lines[i].strip())
    i += 1
    results = []
    while i < len(input_lines):
        if input_lines[i].strip() == '':
            i += 1
            continue
        n = int(input_lines[i].strip())
        i += 1
        coords = [None] * (n + 1)
        for city in range(1, n + 1):
            x, y = map(int, input_lines[i].strip().split())
            coords[city] = (x, y)
            i += 1
        m = int(input_lines[i].strip())
        i += 1
        existing = []
        for _ in range(m):
            u, v = map(int, input_lines[i].strip().split())
            existing.append((u, v))
            i += 1
        result = solve_prim_no_heap(n, coords, existing)
        results.append(result)
    return results

def main():
    input_lines = sys.stdin.read().split('\n')
    results = parse_input(input_lines)
    for idx, result in enumerate(results):
        if result:
            for u, v in result:
                print(f"{u} {v}")
        else:
            print("No new highways need")
        if idx != len(results) - 1:
            print()

if __name__ == "__main__":
    main()
