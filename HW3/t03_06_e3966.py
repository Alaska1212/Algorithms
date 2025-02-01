def search(array, x):
    left = 0
    right = len(array) - 1
    while left <= right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        elif array[m] > x:
            right = m - 1
        else:
            return "YES"
    return "NO"


n = int(input()) #кількисть метеликів
butterflies = list(map(int, input().split())) #види метеликів
m = int(input()) #кількість про яку треба дізнатись
check = list(map(int, input().split())) #метелики, яких треба перевірити

i = 0
while i < m:
    print(search(butterflies, check[i]))
    i += 1


