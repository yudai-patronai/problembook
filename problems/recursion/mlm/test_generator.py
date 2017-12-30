#!/usr/bin/env python3

import os
import shutil
import solution

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
        ans['{0:02}'.format(i)] = (n, solution.mlm(n))
    for key, value in ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1])