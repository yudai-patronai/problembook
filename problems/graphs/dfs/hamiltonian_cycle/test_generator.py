#!/usr/bin/env python3

import os
import sys
import random
import shutil

sys.path.append(os.path.abspath('../..'))
import task

random.seed('hamiltonian_cycle')

def gen_cycle_edges(n):
    l = list(range(n))
    random.shuffle(l)
    edges=[]
    for k in range(-1, n-1):
        if l[k] < l[k+1]:
            edges.append((l[k], l[k+1]))
        else:
            edges.append((l[k+1], l[k]))
    return edges

def gen_graph_edges(n, m):
    g = set(gen_cycle_edges(n))

    for i in range(m):
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
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, 2 * i))
        t += 1

    for i in range(10):
        n = random.randrange(6, 19)
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, n//2))
        t += 1

    for i in range(10):
        n = random.randrange(6, 19)
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, n))
        t += 1

    for i in range(10):
        n = random.randrange(6, 19)
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, 3 * n//2))
        t += 1

    for i in range(10):
        n = random.randrange(6, 19)
        task.gen_test(tests_dir, t, n, gen_graph_edges(n, 6 * n//2))
        t += 1

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
gen_tests(tests_dir)
