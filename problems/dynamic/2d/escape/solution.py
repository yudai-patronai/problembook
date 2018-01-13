n = int(input())
m = int(input())
a = [[int(input()) for _ in range(m)] for _ in range(n)]
d = [[0]*m for _ in range(n)]
d[0][0] = 1
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            continue
        if i == j == 0:
            continue
        elif j == 0:
            d[i][j] = d[i-1][j]
        elif i == 0:
            d[i][j] = d[i][j-1]
        else:
            d[i][j] = d[i-1][j] + d[i][j-1]
if d[n-1][m-1] > 0:
    print(d[n-1][m-1])
else:
    print("Impossible")
