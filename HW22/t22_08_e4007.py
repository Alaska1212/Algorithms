def get_neighbors(num_str):
    neighbors = []
    digits = list(num_str)

    if digits[0] != '9':
        new_digits = digits[:]
        new_digits[0] = str(int(new_digits[0]) + 1)
        neighbors.append(''.join(new_digits))

    if digits[3] != '1':
        new_digits = digits[:]
        new_digits[3] = str(int(new_digits[3]) - 1)
        neighbors.append(''.join(new_digits))

    neighbors.append(num_str[-1] + num_str[:-1])

    neighbors.append(num_str[1:] + num_str[0])

    return [x for x in neighbors if '0' not in x]


def bfs(start, end):
    queue = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}

    index = 0
    while index < len(queue):
        curr = queue[index]
        index += 1

        if curr == end:
            break

        for neighbor in get_neighbors(curr):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = curr
                queue.append(neighbor)

    path = []
    curr = end
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path

start = input().strip()
end = input().strip()

path = bfs(start, end)

for number in path:
    print(number)
