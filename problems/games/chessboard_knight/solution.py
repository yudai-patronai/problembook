def solve(x, y):
    if x >= n or y >= m:
        return True
    if d[x][y] is not None:
        return d[x][y]
    is_win = (not solve(x+2, y+1)) or (not solve(x+1, y+2))

if __name__ == "__main__":
    n, m = map(int, input().split())
    d = [[None] * m for _ in range(n)]
    solve(0, 0)
    if d[0][0]:
        print("YES")
    else:
        print("NO")
