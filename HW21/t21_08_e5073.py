n, m = map(int, input().split())
edges = set()
for _ in range(m):
    u, v = map(int, input().split())
    if (u, v) in edges:
        print("YES")
        break
    edges.add((u, v))
else:
    print("NO")
