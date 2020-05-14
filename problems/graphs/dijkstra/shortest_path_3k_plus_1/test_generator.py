#!/usr/bin/env python3

import os
from lib import random
import shutil

import solution

from lib.graphs import task

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

random.seed('shortest_path_3k_plus_1')


def gen_test_weight_pairs(tests_dir, ind, n, m, pairs):
    print('test %d' % (ind), n, m)
    test = os.path.join(tests_dir, '%.2d' % (ind))
    ans = test + '.a'

    edges = task.add_rand_weight(task.gen_graph_edges(n, m))
    m = len(edges)
    k = len(pairs)

    with open(test, 'w') as f:
        print(n, m, file=f)
        for e in edges:
            print(' '.join(map(str, e)), file=f)
        print(k, file=f)
        for p in pairs:
            print(' '.join(map(str, p)), file=f)

    with open(ans, 'w') as f:
        f.write(solution.solve(task.edges_to_graph(n, edges), pairs))


def gen_manual_test(tests_dir, ind, question_str, answer_str):
    print('test (manual) %d' % (ind))
    test = os.path.join(tests_dir, '%.2d' % (ind))
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(question_str)

    with open(ans, 'w') as f:
        f.write(answer_str)



def gen_tests_weight_pairs(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    gen_manual_test(tests_dir, 1, '2 1\n0 1 81\n1\n0 1\n', '0 1\n')
    gen_manual_test(tests_dir, 2, '4 3\n3 2 73\n2 0 31\n0 1 89\n2\n0 1\n0 3\n', '0 1\n0 2 0 2 3\n')
    t += 2
    for i in range(5):
        n = 2 + i * 2
        gen_test_weight_pairs(tests_dir, t, n, i, [(0, 1)])
        t += 1

    for i in range(1, 5):
        n = 2 + i * 2
        gen_test_weight_pairs(tests_dir, t, n, 0, [(0, 1), (0, 3)])
        t += 1

    for i in range(5):
        n = random.randrange(100, 1000)
        pairs = []
        for i in range(random.randrange(1, 10)):
            pairs.append((random.randrange(n), random.randrange(n)))
        gen_test_weight_pairs(tests_dir, t, n, 5, pairs)
        t += 1

    for i in range(4):
        n = random.randrange(100, 1000)
        pairs = []
        for i in range(random.randrange(1, 10)):
            pairs.append((random.randrange(n), random.randrange(n)))
        gen_test_weight_pairs(tests_dir, t, n, 100, pairs)
        t += 1


gen_tests_weight_pairs(tests_dir)
