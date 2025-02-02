def cyclic_shift(n):
    str = bin(n)[2:]
    array = []
    i = 0
    max = n
    while i < len(str):
        str = str[1:] + str[0]
        array.append(str)
        i += 1
    for el in array:
        if int(el, 2) > max:
            max = int(el, 2)
    return max


n = int(input())
print(cyclic_shift(n))

