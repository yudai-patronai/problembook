#!/usr/bin/env python3

import os
import shutil


def make_test(test_file, m, n, ans):

    with open(test_file, 'w') as f:
        f.write(str(m) + '\n')
        f.write(str(n) + '\n')

    with open(test_file + '.a', 'w') as f:
        f.write(str(ans) + '\n')


if __name__ == '__main__':

    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    boards_ans = {
        '01': (1, 1, 3),
        '02': (4, 0, 13),
        '03': (0, 0, 1),
        '04': (0, 100, 101),
        '05': (1, 0, 2),
        '06': (3, 0, 5),
        '07': (2, 2, 7),
    }

    for key, value in boards_ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1], value[2])
