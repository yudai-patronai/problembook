#!/usr/bin/env python3

import os
import shutil
from lib import random
from queue import Queue


def solver(in_str):
    s, t = map(lambda x: [ord(x[0]) - ord('a'), int(x[1]) - 1], in_str.strip().split())
    d = [[[[-1] * 8 for _ in range(8)] for _ in range(8)] for _ in range(8)]
    d[s[0]][s[1]][t[0]][t[1]] = 0
    moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    q = Queue()
    q.put((s, t))
    while not q.empty():
        s, t = q.get()
        for sx, sy in moves:
            for tx, ty in moves:
                if 0 <= s[0] + sx < 8 and 0 <= s[1] + sy < 8 and 0 <= t[0] + tx < 8 and 0 <= t[1] + ty < 8 and \
                        (d[s[0] + sx][s[1] + sy][t[0] + tx][t[1] + ty] == -1 or d[s[0] + sx][s[1] + sy][t[0] + tx][
                            t[1] + ty] >
                         d[s[0]][s[1]][t[0]][t[1]] + 1):
                    d[s[0] + sx][s[1] + sy][t[0] + tx][t[1] + ty] = d[s[0]][s[1]][t[0]][t[1]] + 1
                    q.put(([s[0] + sx, s[1] + sy], [t[0] + tx, t[1] + ty]))

    ans = -1
    for ix in range(8):
        for iy in range(8):
            if ans == -1 or ans > d[ix][iy][ix][iy] != -1:
                ans = d[ix][iy][ix][iy]
    return ans


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

with open(os.path.join(tests_dir, '{0:0>2}'.format(1)), 'w') as f:
    f.write("{0} {1}\n".format("a1", "a3"))
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(1)), 'w') as f:
    f.write("1\n")

with open(os.path.join(tests_dir, '{0:0>2}'.format(2)), 'w') as f:
    f.write("{0} {1}\n".format("b1", "d8"))
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(2)), 'w') as f:
    f.write("-1\n")

with open(os.path.join(tests_dir, '{0:0>2}'.format(3)), 'w') as f:
    f.write("{0} {1}\n".format("c3", "c3"))
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(3)), 'w') as f:
    f.write("0\n")

for i in range(4, 11):
    ix = random.randint(ord('a'), ord('h'))
    iy = random.randint(0, 7)
    jx = random.randint(ord('a'), ord('h'))
    jy = random.randint(0, 7)

    s = "".join([chr(ix), str(iy)])
    t = "".join([chr(jx), str(jy)])

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0} {1}\n".format(s, t))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write("{}\n".format(solver(" ".join([s, t]))))
