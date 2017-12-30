def recover_path(n, f, ans):
    if n == -1:
        return
    recover_path(f[n], f, ans)
    ans.append(n)


def lis(s):
    n = len(s)
    d = [0 for _ in range(n)]
    f = [-1 for _ in range(n)]
    for i in range(n):
        m = 0
        k = -1
        for j in range(i):
            if s[i] > s[j] and d[j] > m:
                m = d[j]
                k = j
        d[i] = m + 1
        f[i] = k            
    ans = []
    m = 0
    for i in range(1, n):
        if d[i] > d[m]:
            m = i
    recover_path(m, f, ans)
    return [s[i] for i in ans]
