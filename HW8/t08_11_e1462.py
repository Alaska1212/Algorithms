#Хитре сортування

def selection_sort(n, lst):
    for i in range(n - 1, 0, -1):
        maxpos = 0
        for j in range(1, i + 1):
            if lst[maxpos]%10 < lst[j]%10 or (lst[maxpos]%10 == lst[j]%10 and lst[maxpos] < lst[j]):
                maxpos = j
            lst[i], lst[maxpos] = lst[maxpos], lst[i]

    return lst

n = int(input())

lst = []
i = 0
while i < n:
    a = int(input())
    lst.append(a)
    i += 1

print(*selection_sort(n,lst))
