def solve(i):
    if d[i] is not None:
        return d[i]
    used = [False] * (k + 1)
    for j in range(1, k+1):
        if i - j >= 0:
            used[solve(i - j)] = True
    for j in range(k+1):
        if not used[j]:
            d[i] = j
            break
    return d[i]


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = max(a)
    d = [None] * (m + 1)
    solve(m)
    s = 0
    for e in a:
        s ^= d[e]
    if s:
        print("YES")
    else:
        print("NO")
