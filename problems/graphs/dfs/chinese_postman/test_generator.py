#!/usr/bin/env python3

import os
from lib import random
import shutil

from lib.graphs import task

random.seed('chinese_postman')


def gen_tests_weight(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 2 + i * 2
        task.gen_test_weight(tests_dir, t, n, i, add_xy=False)
        t += 1

    for i in range(20):
        n = random.randrange(10, 50)
        task.gen_test_weight(tests_dir, t, n, n, add_xy=False)
        t += 1

    for i in range(20):
        n = random.randrange(50, 100)
        task.gen_test_weight(tests_dir, t, n, n * n, add_xy=False)
        t += 1


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

gen_tests_weight(tests_dir)
