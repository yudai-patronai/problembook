#!/usr/bin/env python3

import os
import sys
import random
import shutil

sys.path.append(os.path.abspath('../..'))
import task

def gen_tests_weight(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    t = 1
    for i in range(5):
        n = 2 + i * 2
        task.gen_test_weight(tests_dir, t, n, i, add_xy = False)
        t += 1

    for i in range(20):
        n = random.randrange(100, 1000)
        task.gen_test_weight(tests_dir, t, n, 5, add_xy = False)
        t += 1

    for i in range(18):
        n = random.randrange(100, 1000)
        task.gen_test_weight(tests_dir, t, n, 100, add_xy = False)
        t += 1

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

gen_tests_weight(tests_dir)
