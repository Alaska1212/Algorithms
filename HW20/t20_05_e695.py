class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size <<= 1
        self.minv = [float('inf')] * (2 * self.size)
        self.maxv = [float('-inf')] * (2 * self.size)

        for i in range(self.n):
            self.minv[self.size + i] = data[i]
            self.maxv[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.minv[i] = min(self.minv[2 * i], self.minv[2 * i + 1])
            self.maxv[i] = max(self.maxv[2 * i], self.maxv[2 * i + 1])

    def update(self, index, value):
        i = self.size + index
        self.minv[i] = self.maxv[i] = value
        i //= 2
        while i:
            self.minv[i] = min(self.minv[2 * i], self.minv[2 * i + 1])
            self.maxv[i] = max(self.maxv[2 * i], self.maxv[2 * i + 1])
            i //= 2

    def query(self, l, r):
        l += self.size
        r += self.size
        min_res = float('inf')
        max_res = float('-inf')
        while l <= r:
            if l % 2 == 1:
                min_res = min(min_res, self.minv[l])
                max_res = max(max_res, self.maxv[l])
                l += 1
            if r % 2 == 0:
                min_res = min(min_res, self.minv[r])
                max_res = max(max_res, self.maxv[r])
                r -= 1
            l //= 2
            r //= 2
        return max_res - min_res


if __name__ == "__main__":
    MAX_N = 100000
    a = [(i * i % 12345 + i * i * i % 23456) for i in range(1, MAX_N + 1)]
    tree = SegmentTree(a)
    k = int(input())
    for _ in range(k):
        x, y = map(int, input().split())
        if x > 0:
            l = x - 1
            r = y - 1
            print(tree.query(l, r))
        else:
            pos = -x - 1
            val = y
            tree.update(pos, val)
