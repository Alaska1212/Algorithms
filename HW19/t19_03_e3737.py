def is_heap(n, arr):
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return "NO"
        if right < n and arr[i] > arr[right]:
            return "NO"

    return "YES"


n = int(input())
arr = list(map(int, input().split()))

print(is_heap(n, arr))
