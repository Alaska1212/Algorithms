def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def prim(n, k, samples):
    used = [False] * n
    min_edge = [float('inf')] * n
    parent = [-1] * n
    min_edge[0] = 0
    total_weight = 0
    edges = []

    for _ in range(n):
        v = -1
        for u in range(n):
            if not used[u] and (v == -1 or min_edge[u] < min_edge[v]):
                v = u

        used[v] = True
        total_weight += min_edge[v]

        if parent[v] != -1:
            edges.append((parent[v], v))

        for to in range(n):
            if not used[to]:
                dist = hamming_distance(samples[v], samples[to])
                if dist < min_edge[to]:
                    min_edge[to] = dist
                    parent[to] = v

    return total_weight, edges

n, k = map(int, input().split())
samples = [input().strip() for _ in range(n)]
total_weight, result_edges = prim(n, k, samples)
print(total_weight)
for u, v in result_edges:
    print(u, v)
