#!/usr/bin/env python3

import os
import random
import solution
import sys
import shutil

MAX_WEIGHT = 20
random.seed(42)


def gen_tree(n):
    return [(random.randint(0, k-1), k) for k in range(1, n)]


def gen_graph(n, m):
    g = set(gen_tree(n))

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

    return [(v1, v2, random.randint(0, MAX_WEIGHT)) for v1, v2 in g]


def graph_edges_to_list(n, graph):
    res = [[] for i in range(n)]
    for a, b, w in graph:
        res[a].append((b, w))
        res[b].append((a, w))

    return res


def gen_test(tests_dir, ind, n, graph):
    print('test %d %d' % (ind, n))
    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'
    m = len(graph)
    start = random.randint(0, n - 1)
    finish = random.randint(0, n - 1)
    if start == finish:
        finish = n - 1 - start
    with open(test, 'w') as f:
        f.write('%d %d ' % (n, m))
        f.write('%d %d\n' % (start, finish))
        for e in graph:
            f.write('%d %d %d\n' % e)

    with open(ans, 'w') as f:
        f.write(solution.solve(graph_edges_to_list(n, graph), start, finish))


def gen_tests(tests_dir):
    t = 1
    for i in range(5):
        gen_test(tests_dir, t, 2 + i * 2, gen_graph(2 + i * 2, i))
        t += 1

    for i in range(5):
        gen_test(tests_dir, t, 2 + i * 2, gen_graph(2 + i * 2, 0))
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        gen_test(tests_dir, t, n, gen_graph(n, 100))
        t += 1

if __name__ == "__main__":
    test_folder = "tests"
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    gen_tests(test_folder)
