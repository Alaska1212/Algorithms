def helper(path, index, min_val, max_val):
    if index == len(path):
        return True

    val = path[index]
    if not (min_val < val < max_val):
        return False

    if index + 1 < len(path):
        next_val = path[index + 1]
        if next_val < val:
            return helper(path, index + 1, min_val, val)
        elif next_val > val:
            return helper(path, index + 1, val, max_val)
        else:
            return False
    else:
        return True

def is_valid_path(path):
    return helper(path, 0, float('-inf'), float('inf'))

if __name__ == "__main__":
    raw_input = input()
    nums = []

    while raw_input.strip() != "":
        nums.extend(map(int, raw_input.strip().split()))
        try:
            raw_input = input()
        except EOFError:
            break

    print("YES" if is_valid_path(nums) else "NO")
