#!/usr/bin/env python3

import os
from lib import random
import shutil


def make_test(test_file, abc, answer):
    
    with open(test_file, 'w') as f:
        for coef in abc:
            f.write(str(coef) + '\n')
    
    with open(test_file + '.a', 'w') as f:
        f.write(str(answer) + '\n')

if __name__ == '__main__':
    
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    
    file_test = {
        '01': ([1, 2, 3], 0),
        '02': ([1, -3, 2], 2),
        '03': ([0, 5, 20], 0),
        '04': ([0, -2, 5], 1),
        '05': ([1, 0, 5], 0),
        '06': ([2, 0, -8], 1),
        '07': ([-5, -6, 0], 0),
        '08': ([-2, 9, 0], 1),
        '09': ([5, 0, 0], 0),
        '10': ([0, 4, 0], 0),
        '11': ([0, 0, -1], 0), 
        '12': ([0, 0, 0], -1), 
        '13': ([-1, 3, -2], 2),
        '14': ([1, -4, 4], 1),
        '15': ([-1, 2, -1], 1),
    }
    
    for key, value in file_test.items():
        make_test(os.path.join(test_folder, key), value[0], value[1])
    
