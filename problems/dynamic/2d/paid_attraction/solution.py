n = int(input())
m = int(input())
a = [[int(input()) for _ in range(m)] for _ in range(n)]
lim = int(input())
d = [[1000000]*m for _ in range(n)]
d[0][0] = 0
for i in range(n):
    for j in range(m):
        if i == j == 0:
            continue
        elif j == 0:
            d[i][j] = d[i-1][j]
        elif i == 0:
            d[i][j] = d[i][j-1]
        else:
            d[i][j] = min(d[i-1][j], d[i][j-1])
        d[i][j] += a[i][j]
if (d[n-1][m-1] <= lim):
    print(lim - d[n-1][m-1])
else:
    print("Impossible")
