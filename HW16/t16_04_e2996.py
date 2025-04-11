n = int(input())
bribe = [0] * n
children = [[] for _ in range(n)]

for i in range(n):
    parts = list(map(int, input().split()))
    bribe[i] = parts[0]
    k = parts[1]
    if k > 0:
        children[i] = [x - 1 for x in parts[2:]]

def dfs(v):
    if not children[v]:
        return bribe[v]
    sub_costs = [dfs(child) for child in children[v]]
    return bribe[v] + min(sub_costs)

print(dfs(0))
