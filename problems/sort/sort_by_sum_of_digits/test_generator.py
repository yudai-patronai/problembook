#!/usr/bin/env python3

import os
import shutil


def make_test(test_file, N, input_array, ans_array):
    with open(test_file, 'w') as f:
        f.write(str(N) + '\n')

        for elem in input_array:
            f.write(str(elem) + '\n')

    with open(test_file + '.a', 'w') as f:
        for elem in ans_array:
            f.write(str(elem) + '\n')


if __name__ == '__main__':

    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    boards_ans = {
        '01': (1, [3], [3]),
        '02': (2, [9, 12], [12, 9]),
        '03': (5, [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        '04': (10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        '05': (5, [100, 1000, 10, 1, 10000], [1, 10, 100, 1000, 10000]),
        '06': (5, [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
        '07': (7, [15, 0, 6, 33, 6, 0, 9], [0, 0, 6, 6, 15, 33, 9]),
        '08': (1, [0], [0]),
        '09': (6, [32, 64, 128, 256, 512, 1024], [32, 1024, 512, 64, 128, 256]),
        '10': (11, [55, 73, 64, 111, 3, 21, 99, 198, 34, 25, 7], [3, 21, 111, 7, 25, 34, 55, 64, 73, 99, 198]),
        '11': (5, [1, 7, 5, 9, 10], [1, 10, 5, 7, 9])
    }

    for key, value in boards_ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1], value[2])
