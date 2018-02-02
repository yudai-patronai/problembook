#!/usr/bin/env python3

import os
import shutil

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

def solve(n):
    if n % 2 != 0:
        return 0

    a = [0] * n
    b = [0] * n

    a[1] = 3
    b[1] = 1

    for i in range(2, n):
        b[i] = a[i - 2] + b[i - 2]
        a[i] = a[i - 2] * 2 + b[i - 2] + b[i]

    return a[n - 1]


def write_test(n):
    write_test.count += 1
    test = os.path.join(tests_dir, '%.2d' % write_test.count)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(str(n) + '\n')

    with open(ans, 'w') as f:
        f.write(str(solve(n)) + '\n')

write_test.count = 0


def gen_tests():
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    write_test(2)
    write_test(4)
    write_test(10)
    write_test(1)
    write_test(117)
    write_test(10000)


gen_tests()
