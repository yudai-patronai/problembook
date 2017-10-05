#!/usr/bin/env python3

import os
from lib import random
import shutil


def make_test(test_file, N, input_lst, answer_lst):
        
    with open(test_file, 'w') as f:
        f.write(str(N) + '\n')
        
        for raw in input_lst:
            for element in raw:
                f.write(str(element) + '\n')
    
    with open(test_file + '.a', 'w') as f:
        for element in answer_lst:
            f.write(str(element) + '\n')


if __name__ == '__main__':
    
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    
    input_test = {
        '01' : (1, [[5]], [5]), 
        '02' : (2, [[1, 1], [1, 1]], [1, 1, 1, 1]),
        '03' : (2, [[1, 2], [3, 4]], [1, 2, 4, 3]),
        '04' : (3, [[1, 2, 5], [1, 0, 8], [2, 1, -1]], 
                [1, 2, 5, 8, -1, 1, 2, 1, 0]),
        '05' : (4, [[1, 2, 20, 4], [21, 2, 1, 6], [0, 2, 1, 8], [4, 5, 3, 7]], 
                [1, 2, 20, 4, 6, 8, 7, 3, 5, 4, 0, 21, 2, 1, 1, 2]),
        '06' : (5, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], 
                    [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 
                    [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7,
                     8, 9, 14, 19, 18, 17, 12, 13]),        
    }
    
    for key, value in input_test.items():
        make_test(os.path.join(test_folder, key), value[0], value[1], value[2])
    
