#!/usr/bin/env python3

import os
from lib import random
import shutil


def make_test(test_file, board, answer):
    
    with open(test_file, 'w') as f:
        for raw in board:
            for element in raw:
                f.write(str(element) + '\n')
    
    with open(test_file + '.a', 'w') as f:
        f.write(str(answer) + '\n')

if __name__ == '__main__':
    
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    
    boards_ans = {
        '01' : ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], -1), 
        '02' : ([[2, 0, 1], [0, 2, 1], [0, 0, 2]], 2),
        '03' : ([[1, 2, 1], [1, 1, 2], [2, 1, 2]], 0),
        '04' : ([[1, 2, 1], [1, 0, 2], [2, 1, 2]], -1),
        '05' : ([[1, 2, 0], [2, 2, 1], [0, 2, 1]], 2),
        '06' : ([[2, 1, 2], [1, 1, 1], [2, 2, 0]], 1),
        '07' : ([[2, 1, 2], [1, 1, 1], [2, 1, 2]], 1),
        '07' : ([[2, 1, 2], [1, 2, 1], [2, 1, 2]], 2),
        '08' : ([[0, 2, 1], [0, 1, 2], [1, 2, 2]], 1),
        '09' : ([[2, 2, 1], [1, 1, 2], [1, 2, 2]], 1),
        '10' : ([[2, 1, 1], [1, 1, 2], [2, 2, 1]], 0),
        
    }
    
    for key, value in boards_ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1])
    
