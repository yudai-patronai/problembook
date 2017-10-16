def place_mine(a, x, y, n, m):
    x -= 1
    y -= 1
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    a[x][y] = -1
    for k in range(8):
        i, j = x+dx[k], y+dy[k]
        if 0 <= i < n and 0 <= j < m and a[i][j] != -1:
            a[i][j] += 1


n = int(input())
m = int(input())
k = int(input())
a = [[0]*m for _ in range(n)]
for _ in range(k):
    i = int(input())
    j = int(input())
    place_mine(a, i, j, n, m)
for line in a:
    for item in line:
        print(item, end=' ')
    print()
