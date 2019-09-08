#!/usr/bin/env python3

from queue import Queue


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    q = Queue()
    d = [[-1]*m for _ in range(n)]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            if a[i][j]:
                d[i][j] = 0
                q.put((i, j))

    while not q.empty():
        x, y = q.get()
        for dx, dy in moves:
            if 0 <= x+dx < n and 0 <= y+dy < m and\
                    d[x+dx][y+dy] == -1:
                d[x+dx][y+dy] = d[x][y] + 1
                q.put((x+dx, y+dy))

    for i in range(n):
        print(*d[i])
