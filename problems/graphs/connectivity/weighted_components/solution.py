def dfs(u, comp):
    used[u] = True
    comp.append(u)
    for v, _ in a[u]:
        if not used[v]:
            dfs(v, comp)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = {{} for i in range(n)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        a[u].add((v, w))
        a[v].add((u, w))
    ans = []
    used = [False] * n
    for i in range(n):
        if not used[i]:
            comp = []
            dfs(u, comp)
            total = 0
            for u in comp:
                for v, w in a[u]:
                    if v > u:
                        total += w
            ans.append(total)
    ans.sort()
    for e in ans:
        print(e)
