def bubble_sort(n , lst):
    count = 0
    for num in range(n-1 , 0, -1):
        for i in range(num):
            if lst[i] > lst[i+1]:
                lst[i] , lst[i+1] = lst[i+1], lst[i]
                count += 1

    return count

n = int(input())
lst = list(map(int , input().split()))
print(bubble_sort(n, lst))
