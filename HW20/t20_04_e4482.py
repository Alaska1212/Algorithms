def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def safe_lcm(a, b):
    return a // gcd(a, b) * b

class SegmentTree:
    def __init__(self, data, op, neutral):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [neutral] * (2 * self.size)
        self.op = op
        self.neutral = neutral
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos, value):
        pos += self.size - 1
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.op(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, l, r):
        l += self.size - 1
        r += self.size - 1
        res = self.neutral
        while l <= r:
            if l % 2 == 1:
                res = self.op(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = self.op(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())

    gcd_tree = SegmentTree(a, gcd, 0)
    lcm_tree = SegmentTree(a, safe_lcm, 1)

    for _ in range(m):
        q, l, r = map(int, input().split())
        if q == 1:
            g = gcd_tree.query(l, r)
            lcm = lcm_tree.query(l, r)
            if g < lcm:
                print("wins")
            elif g > lcm:
                print("loser")
            else:
                print("draw")
        else:
            gcd_tree.update(l, r)
            lcm_tree.update(l, r)
