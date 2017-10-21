#!/usr/bin/env python3

import os
from lib import random
import shutil


def make_test(test_file, input_num, answer):
    
    with open(test_file, 'w') as f:
        f.write(str(input_num) + '\n')
    
    with open(test_file + '.a', 'w') as f:
        f.write(str(answer) + '\n')

if __name__ == '__main__':
    
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    
    file_test = {
        '01': (3, "Fizz"),
        '02': (15, "FizzBuzz"),
        '03': (55, "Buzz"),
        '04': (1001, "Pozz"),
        '05': (30, "FizzBuzz"),
        '06': (26, "Nedelizz"),
        '07': (0, "FizzBuzzPozz"),
        '08': (210, "FizzBuzzPozz"),
        '09': (35, "BuzzPozz"),
        '10': (49, "Pozz"),
        '11': (1, "Nedelizz"),
        '12': (252, "FizzPozz"),
    }
    
    for key, value in file_test.items():
        make_test(os.path.join(test_folder, key), value[0], value[1])
    
