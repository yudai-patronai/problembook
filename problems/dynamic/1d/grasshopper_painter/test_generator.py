#!/usr/bin/env python3

import os
import shutil
import random

random.seed(100)
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

def solve(a, b):
    n = len(a)
    c = [0] * n
    c[0] = 1
    if a[0] == a[1] or b[0] == a[1]:
        c[1] = 1

    for i in range(2, n):
        if a[i - 1] == a[i] or b[i - 1] == a[i]:
            c[i] = c[i - 1]
        if a[i - 2] == a[i] or b[i - 2] == a[i]:
            c[i] = (c[i] + c[i - 2]) % 947

    return c[-1]


def write_test(ar1, ar2):
    write_test.count += 1
    test = os.path.join(tests_dir, '%.2d' % write_test.count)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(str(len(ar1)) + '\n')
        f.write(' '.join(map(str, ar1)) + '\n')
        f.write(' '.join(map(str, ar2)) + '\n')

    with open(ans, 'w') as f:
        f.write(str(solve(ar1, ar2)) + '\n')

write_test.count = 0


def gen_test(n):
    a = [random.randrange(1, 3) for _ in range(n)]
    b = [0] * n
    b[-2] = a[-1]
    for i in range(n - 2):
        if (a[i + 1] != a[i] and a[i + 2] != a[i]) or random.randrange(3) == 0:
            b[i] = 3 - a[i]

    write_test(a, b)


def gen_tests():
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    write_test([1, 2], [0, 0])
    write_test([1, 1, 2, 2], [2, 2, 2, 2])
    write_test(list(range(1, 10)), list(range(2, 11)))
    write_test([1, 1, 1, 2, 2], [2, 1, 0, 0, 0])
    write_test([1, 1, 1, 2, 2, 1, 1, 1],
               [0, 2, 2, 2, 1, 0, 0, 0])
    gen_test(100)
    gen_test(100)
    gen_test(100)
    gen_test(100)
    gen_test(10000)


gen_tests()
