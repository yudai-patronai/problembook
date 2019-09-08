#!/usr/bin/env python3

import os
import shutil
from lib import random
from queue import Queue


def generate_moves(num):
    moves = []
    if num % 10 > 1:
        moves.append(num-1)
    if num // 1000 < 9:
        moves.append(num+1000)
    moves.append(num % 1000 * 10 + num // 1000)
    moves.append(num // 10 + num % 10 * 1000)
    return moves


def solver(s, t):
    d = {}
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    d[i * 1000 + j * 100 + k * 10 + l] = -1
    d[s] = 0
    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in generate_moves(u):
            if d[v] == -1:
                d[v] = d[u] + 1
                q.put(v)

    return d[t] + 1


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

with open(os.path.join(tests_dir, '{0:0>2}'.format(1)), 'w') as f:
    f.write("{0}\n{1}\n".format(1234, 4321))
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(1)), 'w') as f:
    f.write("6\n")

for test in range(2, 10):
    s = int("".join([str(random.randint(1, 9)) for _ in range(4)]))
    t = int("".join([str(random.randint(1, 9)) for _ in range(4)]))

    with open(os.path.join(tests_dir, '{0:0>2}'.format(test)), 'w') as f:
        f.write("{0}\n{1}\n".format(s, t))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(test)), 'w') as f:
        f.write("{}\n".format(solver(s, t)))

with open(os.path.join(tests_dir, '{0:0>2}'.format(10)), 'w') as f:
    f.write("{0}\n{1}\n".format(7536, 7536))
with open(os.path.join(tests_dir, '{0:0>2}.a'.format(10)), 'w') as f:
    f.write("1\n")