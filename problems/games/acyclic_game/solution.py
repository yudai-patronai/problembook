def dfs(u):
    for v in adj_list[u]:
        if states[v] is None:
            dfs(v)
        if not states[v]:
            states[u] = True
            break
    else:
        states[u] = False


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].add(v)

    states = [None] * n
    dfs(k)
    if states[k]:
        print("First")
    else:
        print("Second")
