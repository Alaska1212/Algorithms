def main():
    n, m = map(int, input().split())
    parent = list(map(int, input().split()))
    a1, a2 = map(int, input().split())
    x, y, z = map(int, input().split())

    LOG = 17
    while (1 << LOG) <= n:
        LOG += 1

    tree = [[] for _ in range(n)]
    for i in range(1, n):
        tree[parent[i - 1]].append(i)

    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n

    def dfs(v, p):
        up[v][0] = p
        for i in range(1, LOG):
            if up[v][i - 1] != -1:
                up[v][i] = up[up[v][i - 1]][i - 1]
        for u in tree[v]:
            depth[u] = depth[v] + 1
            dfs(u, v)

    dfs(0, -1)

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        for i in reversed(range(LOG)):
            if up[u][i] != -1 and depth[up[u][i]] >= depth[v]:
                u = up[u][i]
        if u == v:
            return u
        for i in reversed(range(LOG)):
            if up[u][i] != -1 and up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]

    a = [0] * (2 * m + 1)
    a[1], a[2] = a1, a2
    for i in range(3, 2 * m + 1):
        a[i] = (x * a[i - 2] + y * a[i - 1] + z) % n

    res = 0
    u = a[1]
    v = a[2]
    lv = lca(u, v)
    res += lv
    for i in range(2, m + 1):
        u = (a[2 * i - 1] + lv) % n
        v = a[2 * i]
        lv = lca(u, v)
        res += lv

    print(res)

if __name__ == "__main__":
    main()
