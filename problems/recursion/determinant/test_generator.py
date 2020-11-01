#!/usr/bin/env python3

import os
from lib import random
import shutil


def make_test(test_file, n, board, answer):
    with open(test_file, 'w') as f:

        f.write(str(n) + '\n')

        for raw in board:
            f.write(' '.join([str(x) for x in raw]) + '\n')

    with open(test_file + '.a', 'w') as f:
        f.write(str(answer) + '\n')


if __name__ == '__main__':
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    boards_ans = {
        '01': (2, [[1, 0], [0, 1]], '1'),
        '02': (2, [[1, 2], [2, 1]], '-3'),
        '03': (1, [[0]], '0'),
        '04': (1, [[-1]], '-1'),
        '05': (2, [[1, 1], [1, 1]], '0'),
        '06': (2, [[1, 2], [1, 2]], '0'),
        '07': (3, [[1, 2, 3], [4, 5, 6], [7, 8, 0]], '27'),
        '08': (3, [[1, -20, 3], [43, 5, -6], [17, 8, 0]], '2865'),
        '09': (4, [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]], '0'),
        '10': (4, [[-1, -12, 37, 14], [-11, 12, 3, -4], [0, 2, 31, 4], [7, 4, 3, 4]], '-41480'),
        '11': (5, [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], '0'),
        '12': (5, [[4, 6, 2, 1, 5], [1, 0, 5, 2, 4], [3, 2, 6, 2, 4], [4, 5, 2, 3, 2], [3, 2, 0, 3, 6]], '519')
    }

    for key, value in boards_ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1], value[2])
