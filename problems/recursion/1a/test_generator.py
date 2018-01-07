#!/usr/bin/env python3

import os
import shutil


def make_test(test_file, n, ans_array):

    with open(test_file, 'w') as f:
        f.write(str(n) + '\n')

    with open(test_file + '.a', 'w') as f:
        for elem in ans_array:
            f.write(str(elem) + ' ')
        f.write('\n')

if __name__ == '__main__':

    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    boards_ans = {
        '01': (0, [1, 0]),
        '02': (1, [1, 0]),
        '03': (6, [4, 4]),
        '04': (10, [6, 6]),
        '05': (14, [9, 9]),
        '06': (20, [13, 12]),
        '07': (25, [16, 16]),
        '08': (30, [19, 19]),
        '09': (77, [48, 48]),
        '10': (37, [23, 23]),
    }

    for key, value in boards_ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1])
