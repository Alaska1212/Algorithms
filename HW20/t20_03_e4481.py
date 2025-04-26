def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = gcd(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos, value):
        pos += self.size - 1
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = gcd(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, l, r):
        l += self.size - 1
        r += self.size - 1
        res = 0
        while l <= r:
            if l % 2 == 1:
                res = gcd(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = gcd(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    st = SegmentTree(a)
    for _ in range(m):
        q, l, r = map(int, input().split())
        if q == 1:
            print(st.query(l, r))
        else:
            st.update(l, r)
