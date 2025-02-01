def find_first(array, x):
    res = - 1
    left = 0
    right = len(array) - 1
    while left <= right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        elif array[m] > x:
            right = m - 1
        else:
            res = m
            right = m -1
    return res

def find_last(array, x):
    res = - 1
    left = 0
    right = len(array) - 1
    while left <= right:
        m = left + (right - left) // 2
        if array[m] < x:
            left = m + 1
        elif array[m] > x:
            right = m - 1
        else:
            res = m
            left = m + 1
    return res

def result(array , x):
    first = find_first(array, x)
    last = find_last(array, x)
    if first == -1:
        return 0
    return last - first + 1



n = int(input()) #кількість тварин
animals = list(map(int, input().split())) #види тварин
m = int(input()) #кількіть запитів
find = list(map(int, input().split())) #запити

i = 0
while i < m:
    print(result(animals, find[i]))
    i += 1
