

def calculate_by_polish(expression: int):
    stack = []
    tokens = expression.split()
    for token in tokens:
        try:
            num = int(token)
            stack.append(num)
        except ValueError:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

    return stack[0]

if __name__ == "__mane__":
    expression = input().strip()
    print(calculate_by_polish(expression))
