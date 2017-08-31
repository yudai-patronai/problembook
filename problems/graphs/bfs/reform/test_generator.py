#!/usr/bin/env python3

import os
import random
import shutil

from lib.graphs import task

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')


def gen_tests_weight_centers(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 2 + i * 2
        task.gen_test_weight_centers(tests_dir, t, n, i, [0, 1])
        t += 1

    for i in range(1, 5):
        n = 2 + i * 2
        task.gen_test_weight_centers(tests_dir, t, n, 0, [0, 1, 2])
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        centers = random.sample(range(n), random.randrange(n // 5) + 1)
        task.gen_test_weight_centers(tests_dir, t, n, 5, centers)
        t += 1

    for i in range(2):
        n = random.randrange(100, 1000)
        centers = random.sample(range(n), random.randrange(n // 2) + 1)
        task.gen_test_weight_centers(tests_dir, t, n, 10, centers)
        t += 1

    for i in range(18):
        n = random.randrange(100, 1000)
        centers = random.sample(range(n), random.randrange(n // 2) + 1)
        task.gen_test_weight_centers(tests_dir, t, n, 100, centers)
        t += 1

    n = 1000
    full = [(b, a) for a in range(1, n) for b in range(a)][:100000]
    task.gen_test(tests_dir, t, n, task.add_rand_weight(full), 0)
    t += 1
    task.gen_test(tests_dir, t, n, task.add_rand_weight(full), *list(range(100)))
    t += 1


gen_tests_weight_centers(tests_dir)
