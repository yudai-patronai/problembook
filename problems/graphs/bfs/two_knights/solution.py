#!/usr/bin/env python3
from queue import Queue


if __name__ == "__main__":
    s, t = map(lambda x: [ord(x[0])-ord('a'), int(x[1])-1],
               input().strip().split())
    d = [[[[-1]*8 for _ in range(8)] for _ in range(8)] for _ in range(8)]
    d[s[0]][s[1]][t[0]][t[1]] = 0
    moves = [(1, 2), (2, 1), (2, -1), (1, -2),
             (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    q = Queue()
    q.put((s, t))
    while not q.empty():
        s, t = q.get()
        for sx, sy in moves:
            for tx, ty in moves:
                if 0 <= s[0]+sx < 8 and 0 <= s[1]+sy < 8 and \
                        0 <= t[0]+tx < 8 and 0 <= t[1]+ty < 8 and \
                        d[s[0]+sx][s[1]+sy][t[0]+tx][t[1]+ty] == -1:
                    d[s[0] + sx][s[1] + sy][t[0] + tx][t[1] + ty] = \
                        d[s[0]][s[1]][t[0]][t[1]] + 1
                    q.put(([s[0]+sx, s[1]+sy], [t[0]+tx, t[1]+ty]))

    ans = -1
    for ix in range(8):
        for iy in range(8):
            if ans == -1 or ans > d[ix][iy][ix][iy] != -1:
                ans = d[ix][iy][ix][iy]
    print(ans)
