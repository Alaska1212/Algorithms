def drying(n, a, k):
    left, right = 0, max(a)

    if k == 1:
        return right

    while right - left > 1:
        middle = (right + left) // 2
        dry = 0     #додаткові хвилини для батареї

        for i in range(n):
            if a[i] > middle:       #якщо річ має більше води, то треба батарея
                dry += (a[i] - middle + k - 2) // (k - 1)
            if dry > middle:
                break

        if dry > middle:
            left = middle
        else:
            right = middle

    return right


n = int(input())
a = list(map(int, input().split()))
k = int(input())

print(drying(n, a, k))
