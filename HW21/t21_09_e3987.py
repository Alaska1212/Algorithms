n, m = map(int, input().split())
edges = set()
for _ in range(m):
    u, v = map(int, input().split())
    if u != v:
        edges.add((min(u, v), max(u, v)))

required = n * (n - 1) // 2
print("YES" if len(edges) == required else "NO")
