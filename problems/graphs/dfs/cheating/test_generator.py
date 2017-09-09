#!/usr/bin/env python3

import os
from lib import random
import shutil

from lib.graphs import task

random.seed('cheating')


def gen_bigraph(n, m):
    l = list(range(n))
    random.shuffle(l)
    k = random.randrange(1, n - 1)
    left, right = l[:k], l[k:]

    avail_edges = []
    for p in left:
        for q in right:
            if p > q:
                avail_edges.append((q, p))
            else:
                avail_edges.append((p, q))

    random.shuffle(avail_edges)

    return set(avail_edges[:min(m, len(avail_edges))])


def gen_graph_edges(n, m, k):
    g = gen_bigraph(n, m)

    for i in range(k):
        a = random.randrange(n)
        b = random.randrange(n - 1)
        if a == b:
            b = n - 1
        if a > b:
            a, b = b, a
        g.add((a, b))

    g = list(g)
    for i in range(len(g)):
        if random.random() < 0.5:
            g[i] = g[i][::-1]

    random.shuffle(g)

    return g


def gen_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 3 + i * 2
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, 2 * i, 0))
        t += 1

    for i in range(5):
        n = 3 + i * 2
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, 2 * i, 2 * i))
        t += 1

    for i in range(10):
        n = random.randrange(100, 1000)
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, 100, 0))
        t += 1

    for i in range(10):
        n = random.randrange(100, 1000)
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, 100, 100))
        t += 1

    for i in range(10):
        n = random.randrange(100, 1000)
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, 10000, 0))
        t += 1

    for i in range(10):
        n = random.randrange(100, 1000)
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, 10000, 1000))
        t += 1


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
gen_tests(tests_dir)
