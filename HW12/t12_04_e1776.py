def rails(n, order):
    stack, current = [], 1
    for wagon in order:
        while current <= n and (not stack or stack[-1] != wagon):
            stack.append(current)
            current += 1
        if stack and stack[-1] == wagon:
            stack.pop()
        else:
            return "No"
    return "Yes"

def process_case():
    results = []
    while True:
        line = input().strip()
        if line == "0":
            break
        order = list(map(int, line.split()))
        results.append(rails(len(order), order))
    return "\n".join(results)

if __name__ == "__main__":
    output = []
    while True:
        n = int(input().strip())
        if n == 0:
            break
        output.append(process_case())
    print("\n".join(output))