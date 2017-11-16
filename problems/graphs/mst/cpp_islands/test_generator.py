#!/usr/bin/env python3

from lib import random
from lib.testgen import TestSet
#from lib.graphs.task import gen_graph_edges

random.seed(42)


def gen_tree_edges(n):
    return [(random.randint(0, k-1), k) for k in range(1, n)]

def gen_graph_edges(n, m, connective=True):
    g = set(gen_tree_edges(n)) if connective else set()

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


def solve(n, edges):
    comp = [i for i in range(n)]
    n_comp = n
    components = [[i] for i in range(n)]
    for i, edge in enumerate(edges, start=1):
        start, end = edge
        a = comp[start]
        b = comp[end]
        if a != b:
            n_comp -= 1
            if n_comp == 1:
                break
            if len(components[a]) < len(components[b]):
                a, b = b, a

            for v in components[b]:
                comp[v] = a

            components[a].extend(components[b])
            components[b] = []
    return i


def gen_test(n, edges):
    q_str = '{} {}\n'.format(n, len(edges))
    q_str += '\n'.join('{} {}'.format(*e) for e in edges)

    a_str = str(solve(n, edges))

    return q_str, a_str


tests = TestSet()

for i in range(16):
    n = 2 + i * 2
    tests.add(*gen_test(n, gen_graph_edges(n, i)))

for i in range(8):
    n = 2 + i * 2
    tests.add(*gen_test(n, gen_graph_edges(n, 0)))

for i in range(4):
    n = random.randrange(100, 1000)
    tests.add(*gen_test(n, gen_graph_edges(n, 100)))

for i in range(2):
    n = random.randrange(100, 1000)
    tests.add(*gen_test(n, gen_graph_edges(n, 10000)))

