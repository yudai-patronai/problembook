#!/usr/bin/env python3

import os
import shutil
from lib import random
from lib.graphs import gen_graph_edges, edges_to_graph


def solve(n, edges, x):
    m = len(edges)
    d = [float("inf")] * n
    d[s] = 0
    for i in range(n):
        for u, v, w in edges:
            if d[v] > d[u] + w:
                d[v] = (d[u] + w if i != n-1 else float("inf"))
    
    return [(v if v != float("inf") else "UDF") for v in d]


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
        f.write(solve(n, edges, *args))


def add_rand_weight(edges):
    return [(a, b, random.randrange(-1000, 1000)) for a, b in edges]


def gen_test_weight(tests_dir, t, n, e):
    gen_test(tests_dir, t, n, add_rand_weight(gen_graph_edges(n, e, connective=False)), random.randrange(n))


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

t = 1
for i in range(5):
    n = 2 + i * 2
    gen_test_weight(tests_dir, t, n, i)
    t += 1

for i in range(5):
    n = 2 + i * 2
    gen_test_weight(tests_dir, t, n, 0)
    t += 1

for i in range(5):
    n = random.randrange(100, 1000)
    gen_test_weight(tests_dir, t, n, 5)
    t += 1

for i in range(2):
    n = random.randrange(100, 1000)
    gen_test(tests_dir, t, n, 10, 5)
    t += 1

for i in range(5):
    n = random.randrange(100, 1000)
    gen_test_weight(tests_dir, t, n, 100)
    t += 1