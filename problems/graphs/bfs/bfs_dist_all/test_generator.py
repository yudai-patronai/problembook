#!/usr/bin/env python3

import os
from lib import random
import shutil

import solution

from lib.graphs import task

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

random.seed('bfs_dist_all')


def gen_test_random(tests_dir, ind, n, m):
    print('test %d' % (ind), n, m)
    test = os.path.join(tests_dir, '%.2d' % (ind))
    ans = test + '.a'

    edges = [(a, b) for a, b in task.gen_graph_edges(n, m)]
    m = len(edges)

    with open(test, 'w') as f:
        print(n, m, file=f)
        for e in edges:
            print(' '.join(map(str, e)), file=f)

    with open(ans, 'w') as f:
        f.write(solution.solve(task.edges_to_graph(n, edges)))


def gen_manual_test(tests_dir, ind, question_str, answer_str):
    print('test (manual) %d' % (ind))
    test = os.path.join(tests_dir, '%.2d' % (ind))
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(question_str)

    with open(ans, 'w') as f:
        f.write(answer_str)



def gen_tests_all(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    gen_manual_test(tests_dir, 1, '2 1\n1 0\n', '0\n1\n')
    gen_manual_test(tests_dir, 2, '6 7\n2 3\n2 0\n5 2\n1 0\n1 2\n5 1\n4 1\n', '0\n1\n1\n2\n2\n2\n')
    t += 2
    for i in range(1, 6):
        n = 2 + i * 2
        gen_test_random(tests_dir, t, n, i)
        t += 1

    for i in range(1, 5):
        n = 2 + i * 2
        gen_test_random(tests_dir, t, n, 0)
        t += 1

    for i in range(5):
        n = random.randrange(100, 1000)
        gen_test_random(tests_dir, t, n, 5)
        t += 1

    for i in range(4):
        n = random.randrange(100, 1000)
        gen_test_random(tests_dir, t, n, 100)
        t += 1


gen_tests_all(tests_dir)
