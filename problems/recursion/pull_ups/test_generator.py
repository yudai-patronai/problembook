#!/usr/bin/env python3

import os
import shutil
import solution

def make_test(test_file, k, m, answer):
    with open(test_file, 'w') as f:
        f.write(str(k) + '\n')
        f.write(str(m) + '\n')
    with open(test_file + '.a', 'w') as f:
        f.write(str(answer) + '\n')

if __name__ == '__main__':
    
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    pairs = [
        (4, 2),
        (1, 10),
        (5, 100),
        (999, 13),
        (1, 1),
        (32, 3),
        (1000, 500)
    ]
    ans = {}
    for i, pair in enumerate(pairs):
        k, m = pair
        ans['{0:02}'.format(i)] = (k, m, solution.pulls(k, m))
    for key, value in ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1], value[2])