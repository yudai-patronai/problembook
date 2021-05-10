#!/usr/bin/env python3

import os, shutil

from lib.graphs import task
from lib import random


def gen_tests_weight_xy(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 2 + i * 2
        task.gen_test_weight(tests_dir, t, n, i)
        t += 1

    for i in range(5):
        n = 2 + i * 2
        task.gen_test_weight(tests_dir, t, n, 0)
        t += 1

    for i in range(5):
        n = random.randrange(100, 1000)
        task.gen_test_weight(tests_dir, t, n, 5)
        t += 1

    for i in range(2):
        n = random.randrange(100, 1000)
        task.gen_test_weight_xy(tests_dir, t, n, 10, 5, 5)
        t += 1

    for i in range(8):
        n = random.randrange(100, 1000)
        task.gen_test_weight(tests_dir, t, n, 100)
        t += 1


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
gen_tests_weight_xy(tests_dir)
