#!/usr/bin/env python3

import os
import shutil


def make_test(test_file, money, coins, ans):

    with open(test_file, 'w') as f:
        f.write(str(money) + '\n')
        f.write(" ".join(map(str, coins)))

    with open(test_file + '.a', 'w') as f:
        f.write(str(ans) + '\n')


if __name__ == '__main__':

    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    boards_ans = {
        '01': (4, [1, 2], 3),
        '02': (10, [5, 2, 3], 4),
        '03': (1, [2], 0),
        '04': (1, [1, 2], 1),
        '05': (1, [2, 1], 1),
        '06': (2, [1, 2], 2),
        '07': (7, [1], 1),
        '08': (7, [1, 2, 3, 4, 5, 6, 7], 15),
        '09': (7, [1, 2, 3, 4, 5, 6, 7, 8], 15),
        '10': (5, [], 0),
        '11': (100, [1, 2, 3, 4, 5], 46262),
        '12': (10, [4, 7], 0),
        '13': (20, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 530)
    }

    for key, value in boards_ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1], value[2])
