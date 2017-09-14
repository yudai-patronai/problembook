#!/usr/bin/env python3

import os
import shutil
import random

random.seed(100)
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')


def gen_test(tests_dir, ind, n):
    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(str(n) + '\n')

    with open(ans, 'w') as f:
        if ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0):
            f.write('YES\n')
        else:
            f.write('NO\n')


def gen_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    gen_test(tests_dir, 1, 1)
    gen_test(tests_dir, 2, 2000)
    gen_test(tests_dir, 3, 400)
    t = 4
    for i in range(10):
        gen_test(tests_dir, t, random.randrange(1, 50000))
        t += 1
        gen_test(tests_dir, t, random.randrange(4, 50000, 4))
        t += 1
        gen_test(tests_dir, t, random.randrange(100, 50000, 100))
        t += 1
        gen_test(tests_dir, t, random.randrange(400, 50000, 400))
        t += 1


gen_tests(tests_dir)
