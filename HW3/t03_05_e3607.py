def find(array, a, b):
    k = 0
    for i in range(0, len(array)):
        if a <=  array[i] and b >=  array[i]:
            k += 1
    return k


f = open("input.txt")
while True:
    n = f.readline()
    if n == "":
        break
    array = [int(x) for x in f.readline().split()]
    a ,b = [int(x) for x in f.readline().split()]
    print(find(array, a, b))
f.close()

