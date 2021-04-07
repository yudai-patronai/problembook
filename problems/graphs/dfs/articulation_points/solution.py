
def dfs(u, p=-1):
    global t
    tin[u] = t
    fup[u] = t
    t += 1
    children = 0
    for v in adj_list[u]:
        if tin[v] == -1:
            dfs(v, u)
            children += 1
            fup[u] = min(fup[u], fup[v])
            if fup[v] >= tin[u] and p != -1:
                cutpoints.add(u+1)
        elif p != v:
            fup[u] = min(fup[u], tin[v])
    if p == -1 and children > 1:
        cutpoints.add(u+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(lambda x: int(x)-1, input().split())
        adj_list[u].add(v)
        adj_list[v].add(u)

    cutpoints = set()
    t = 0
    tin = [-1] * n
    fup = [-1] * n
    for i in range(n):
        if tin[i] == -1:
            dfs(i)

    if cutpoints:
        print(" ".join(map(str, sorted(cutpoints))))
    else:
        print(-1)
