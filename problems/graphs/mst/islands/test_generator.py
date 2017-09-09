#!/usr/bin/env python3


import os
from lib import random
import shutil

import solution

from lib.graphs.task import gen_graph_edges

random.seed(42)


def gen_test(tests_dir, ind, n, edges):
    m = len(edges)
    params = ' '.join(map(str, (n, m)))
    print('test %d ' % ind + params)

    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(params + '\n')
        for e in edges:
            f.write(' '.join(map(str, e)) + '\n')

    with open(ans, 'w') as f:
        f.write(solution.solve(n, edges))


def gen_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 2 + i * 2
        gen_test(tests_dir, t, n, gen_graph_edges(n, i))
        t += 1

    for i in range(5):
        n = 2 + i * 2
        gen_test(tests_dir, t, n, gen_graph_edges(n, 0))
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test(tests_dir, t, n, gen_graph_edges(n, 100))
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test(tests_dir, t, n, gen_graph_edges(n, 10000))
        t += 1


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
gen_tests(tests_dir)
