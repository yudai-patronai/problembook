def dfs(u):
    d[u] = "UDF"
    for v, _ in a[u]:
        if d[v] != "UDF":
            dfs(v)


if __name__ == "__main__":
    n, m, s = map(int, input().strip().split())
    edges = []
    a = {i: [] for i in range(n)}
    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        edges.append((u, v, w))
        a[u].append((v, w))
    d = [float("inf")] * n
    d[s] = 0
    p = [-1] * n
    on_cycle = None
    for i in range(n):
        for u, v, w in edges:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                p[v] = u
                if i == n-1:
                    on_cycle = v
                    break

    if on_cycle is not None:
        for _ in range(n):
            on_cycle = p[on_cycle]
        dfs(on_cycle)

    for i in range(n):
        if d[i] == float("inf"):
            d[i] = "UDF"

    print(' '.join(map(str, d)))
