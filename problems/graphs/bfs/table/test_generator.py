#!/usr/bin/env python3

import os
import shutil
from lib import random
from queue import Queue


def solver(n, m, a):
    q = Queue()
    d = [[-1] * m for _ in range(n)]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            if a[i][j]:
                d[i][j] = 0
                q.put((i, j))

    while not q.empty():
        x, y = q.get()
        for dx, dy in moves:
            if 0 <= x + dx < n and 0 <= y + dy < m and \
                    d[x + dx][y + dy] == -1:
                d[x + dx][y + dy] = d[x][y] + 1
                q.put((x + dx, y + dy))

    return d


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

with open(os.path.join(tests_dir, '{0:0>2}'.format(1)), 'w') as f:
    f.write("{0} {1}\n".format(2, 3))
    f.write("0 0 1\n")
    f.write("1 0 0\n")
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(1)), 'w') as f:
    f.write("1 1 0\n")
    f.write("0 1 1\n")

with open(os.path.join(tests_dir, '{0:0>2}'.format(2)), 'w') as f:
    f.write("{0} {1}\n".format(1, 1))
    f.write("1\n")
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(2)), 'w') as f:
    f.write("0\n")


for test in range(3, 11):
    n = random.randint(1, 500)
    m = random.randint(1, 500)

    a = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]

    with open(os.path.join(tests_dir, '{0:0>2}'.format(test)), 'w') as f:
        f.write("{0} {1}\n".format(n, m))
        for i in range(n):
            f.write(" ".join(map(str, a[i])) + "\n")
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(test)), 'w') as f:
        d = solver(n, m, a)
        for i in range(n):
            f.write(" ".join(map(str, d[i])) + "\n")
