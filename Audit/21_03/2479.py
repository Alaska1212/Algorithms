BRACKETS = {"(": ")", "[": "]"}


def check(sequence: str) -> bool:
    stack = []
    for bracket in sequence:
        if bracket in BRACKETS:  
            stack.append(bracket)
        elif stack and bracket == BRACKETS[stack[-1]]:  
            stack.pop()
        else:
            return False  
    return not stack


if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        print("Yes" if check(input().strip()) else "No")