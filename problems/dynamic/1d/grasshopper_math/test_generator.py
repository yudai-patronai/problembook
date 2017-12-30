#!/usr/bin/env python3

import os
import shutil
import random

random.seed(100)
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

def solve(a):
    n = len(a)
    b = [0] * n
    b[0] = 1

    for i in range(0, n - 1):
        b[i + 1] = (b[i + 1] + b[i]) % 937
        if a[i] > 1 and i + a[i] < n:
            b[i + a[i]] = (b[i + a[i]] + b[i]) % 937

    return b[-1]


def write_test(ar):
    write_test.count += 1
    test = os.path.join(tests_dir, '%.2d' % write_test.count)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(str(len(ar)) + '\n')
        f.write(' '.join(map(str, ar)) + '\n')

    with open(ans, 'w') as f:
        f.write(str(solve(ar)) + '\n')

write_test.count = 0


def gen_test(n, a, b):
    write_test([random.randrange(a, b) for _ in range(n)])


def gen_tests():
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    write_test([1,1])
    write_test([2,2,1])
    write_test([1] * 10)
    write_test([2] * 10)
    write_test([10] * 10)
    write_test(list(range(10, 0, -1)) + [1])
    gen_test(100, 1, 5)
    gen_test(100, 1, 100)
    gen_test(10000, 1, 5)


gen_tests()
