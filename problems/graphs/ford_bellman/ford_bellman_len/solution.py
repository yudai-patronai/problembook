if __name__ == "__main__":
    n, m, s = map(int, input().strip().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        edges.append((u, v, w))
    d = [float("inf")] * n
    d[s] = 0
    changed = [False] * n
    for i in range(n):
        for u, v, w in edges:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                if i == n-1:
                    changed[v] = True

    for i in range(n):
        if changed[i] or d[i] == float("inf"):
            d[i] = "UDF"
    print(' '.join(map(str, d)))
