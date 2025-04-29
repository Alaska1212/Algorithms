class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)

    def add(self, i, x):
        while i <= self.n:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    ft = FenwickTree(n)
    for i in range(n):
        ft.add(i + 1, a[i])

    for _ in range(q):
        parts = input().split()
        if parts[0] == '+':
            i = int(parts[1])
            d = int(parts[2])
            ft.add(i, d)
        else:
            f = int(parts[1])
            t = int(parts[2])
            print(ft.range_sum(f, t))

solve()
