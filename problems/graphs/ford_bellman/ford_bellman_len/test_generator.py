#!/usr/bin/env python3

import os
import shutil
from lib import random


def solve(n, edges, s):
    m = len(edges)
    d = [float("inf")] * n
    d[s] = 0
    changed = [False] * n
    for i in range(n):
        for u, v, w in edges:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                if i == n-1:
                    changed[v] = True
    
    for i in range(n):
        if changed[i] or d[i] == float("inf"):
            d[i] = "UDF"    
    return d


def gen_graph_edges(n, m):
    g = set()

    for i in range(m):
        a = random.randrange(n)
        b = random.randrange(n - 1)
        if a > b:
            a, b = b, a
        elif a == b:
            b = n - 1
        g.add((a, b))

    g = list(g)
    for i in range(len(g)):
        if random.random() < 0.5:
            g[i] = g[i][::-1]

    random.shuffle(g)

    return g


def gen_test(tests_dir, ind, n, edges, *args, **kwargs):
    m = len(edges)
    params = ' '.join(map(str, (n, m) + args))
    print('test %d ' % ind + params)

    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(params + '\n')
        for e in edges:
            f.write(' '.join(map(str, e)) + '\n')

    with open(ans, 'w') as f:
        f.write(' '.join(map(str, solve(n, edges, *args))))


def add_rand_weight(edges):
    return [(a, b, random.randint(-500, 1000)) for a, b in edges]


def gen_test_weight(tests_dir, t, n, e):
    gen_test(tests_dir, t, n, add_rand_weight(gen_graph_edges(n, e)), random.randrange(n))


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

t = 1
for i in range(10):
    n = 2 + i * 2
    gen_test_weight(tests_dir, t, n, random.randint(i + 1, n * (n - 1)))
    t += 1

for i in range(5):
    n = random.randrange(100, 1000)
    gen_test_weight(tests_dir, t, n, 50)
    t += 1

for i in range(5):
    n = random.randrange(100, 1000)
    gen_test_weight(tests_dir, t, n, random.randint(100, 1000))
    t += 1

gen_test(tests_dir, 21, 3, [(0, 1, -4), (1, 2, 4), (2, 0, -1)], 0)