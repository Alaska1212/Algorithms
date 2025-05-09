import math

def dist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx * dx + dy * dy)

def main():
    N, R = map(int, input().split())
    villages = [tuple(map(int, input().split())) for _ in range(N)]

    coverage = []
    for i in range(N):
        covers = set()
        for j in range(N):
            if dist(villages[i], villages[j]) <= R:
                covers.add(j)
        coverage.append(covers)

    uncovered = set(range(N))
    selected = []

    while uncovered:
        best = -1
        best_cover = set()
        for i in range(N):
            current_cover = coverage[i] & uncovered
            if len(current_cover) > len(best_cover):
                best_cover = current_cover
                best = i
        selected.append(best)
        uncovered -= best_cover

    selected.sort()

    print(len(selected))
    print(' '.join(str(i + 1) for i in selected))

main()
