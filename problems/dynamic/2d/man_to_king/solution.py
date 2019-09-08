if __name__ == "__main__":
    x, y = map(lambda x: int(x)-1, input().strip().split())
    d = [[0]*8 for _ in range(8)]
    d[y][x] = 1
    for i in range(y+1, 8):
        for j in range(8):
            if j-1 >= 0:
                d[i][j] += d[i-1][j-1]
            if j+1 < 8:
                d[i][j] += d[i-1][j+1]
    print(sum(d[7]))
