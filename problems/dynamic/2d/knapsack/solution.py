n = int(input())
s = int(input())
w = []
p = []
for _ in range(n):
    w.append(int(input()))
    p.append(int(input()))
d = [[0]*(s+1) for _ in range(n+1)]
for i in range(n):
    for j in range(1, s+1):
        d[i+1][j] = d[i][j]
        if j >= w[i]:
            d[i+1][j] = max(d[i+1][j], d[i][j-w[i]]+p[i])
print(d[n][s])
