def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    tree = [0] * (n + 1)

    def add(i, x):
        while i <= n:
            tree[i] += x
            i += i & -i

    def sum_to(i):
        res = 0
        while i > 0:
            res += tree[i]
            i -= i & -i
        return res

    for idx, val in enumerate(a):
        add(idx + 1, val)

    for _ in range(q):
        parts = input().split()
        if parts[0] == '?':
            f = int(parts[1])
            t = int(parts[2])
            res = sum_to(t) - sum_to(f - 1)
            print(res)
        else:  # '='
            i = int(parts[1])
            d = int(parts[2])
            diff = d - a[i - 1]
            a[i - 1] = d
            add(i, diff)

solve()
