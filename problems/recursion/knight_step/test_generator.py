#!/usr/bin/env python3

import os
import shutil


def make_test(test_file, case, ans):

    with open(test_file, 'w') as f:
        f.write('\n'.join(map(str, case)))
    with open(test_file + '.a', 'w') as f:
        f.write(str(ans))

if __name__ == '__main__':

    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)

    boards_ans = {
        '01': ((1,1,1,1), 0),
        '02': ((1,1,2,3), 1),
        '03': ((1,1,3,2), 1),
        '04': ((1,1,1,3), 2),
        '05': ((1,1,3,1), 2),
        '06': ((1,1,4,4), 2),
        '07': ((1,1,1,2), -1),
        '08': ((1,1,2,2), -1),
        '09': ((1,1,8,8), -1),
        '10': ((4,4,1,2), -1),
        '11': ((4,4,8,8), -1),
        '12': ((4,4,8,6), 2),
        '13': ((4,4,1,1), 2),
        '14': ((4,3,2,7), 2),
        '15': ((4,3,3,5), 1),
    }

    for key, value in boards_ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1])
