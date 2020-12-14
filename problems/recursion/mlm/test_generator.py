#!/usr/bin/env python3

import os
import shutil


def solve(n):
    d = [0] * n
    d[0] = 40
    for i in range(1, n):
        f = (d[i-1] - 10) / 0.3 * 0.7
        d[i] = (2 * f + 100) * 0.3 + 10
    return d[-1]


def make_test(test_file, n, answer):
    with open(test_file, 'w') as f:
        f.write(str(n) + '\n')
    with open(test_file + '.a', 'w') as f:
        f.write(str(int(answer)) + '\n')


if __name__ == '__main__':
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    ns = [
        (1),
        (20),
        (2),
        (4),
        (10),
        (12),
        (55)
    ]
    ans = {}
    for i, n in enumerate(ns):
        ans['{0:02}'.format(i)] = (n, solve(n))
    for key, value in ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1])