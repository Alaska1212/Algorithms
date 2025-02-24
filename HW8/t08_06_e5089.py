#Словник

def insertion_sort(array, n):
    for index in range(1, n):
        currentValue = array[index]
        position = index
        while position > 0:
            if array[position - 1] > currentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1
        array[position] = currentValue
    return array


n = int(input())
words = [input().strip() for _ in range(n)]
for i in insertion_sort(words , n):
    print(i)
