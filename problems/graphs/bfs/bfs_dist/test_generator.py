#!/usr/bin/env python3

import os
from lib import random

from lib.graphs import task

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')


def gen_tests(tests_dir):
    if not os.path.exists(tests_dir):
        os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 2 + i * 2
        task.gen_test(tests_dir, t, n, task.gen_graph_edges(n, i),
                      random.randrange(n), random.randrange(n))
        t += 1

    for i in range(5):
        n = 4 + i * 2
        task.gen_test(tests_dir, t, n, task.gen_graph_edges(n, 0),
                      random.randrange(n), random.randrange(n))
        t += 1

    for i in range(5):
        n = random.randrange(100, 1000)
        task.gen_test(tests_dir, t, n, task.gen_graph_edges(n, 5),
                      random.randrange(n), random.randrange(n))
        t += 1

    for i in range(2):
        n = random.randrange(100, 1000)
        task.gen_test(tests_dir, t, n, task.gen_graph_edges(n, 10), 5, 5)
        t += 1

    for i in range(8):
        n = random.randrange(100, 1000)
        task.gen_test(tests_dir, t, n, task.gen_graph_edges(n, 100),
                      random.randrange(n), random.randrange(n))
        t += 1


gen_tests(tests_dir)
