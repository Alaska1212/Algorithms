def cat(d: int):
    if d < 10:
        return str(d)
    else:
        return chr(ord('A') - 10 + d)

def convert(num: str, from_base: int, to_base: int):
    stack = []

    decimal = 0
    for d in num:
        decimal = decimal * from_base + int(d, from_base)

    while decimal > 0:
        d = decimal % to_base
        decimal //= to_base
        stack.append(d)

    res = ""
    while stack:
        res += cat(stack.pop())
    return res





if __name__ == "__main__":
    print(convert(input(), 2, 16))