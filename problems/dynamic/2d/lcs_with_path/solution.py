def recover_path(n, m, f, ans):
    if f[n][m] == -1:
        return
    recover_path(f[n][m][0], f[n][m][1], f, ans)
    if f[n][m] == (n-1, m-1):
        ans.append(n-1)


def lcs(s1, s2):
    n, m = len(s1), len(s2)
    d = [[0]*(m+1) for _ in range(n+1)]
    f = [[-1]*(m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                d[i+1][j+1] = d[i][j] + 1
                f[i+1][j+1] = (i, j)
            elif d[i][j+1] > d[i+1][j]:
                d[i+1][j+1] = d[i][j+1]
                f[i+1][j+1] = (i, j+1)
            else:
                d[i+1][j+1] = d[i+1][j]
                f[i+1][j+1] = (i+1, j)
    ans = []
    recover_path(n, m, f, ans)
    return [s1[i] for i in ans]