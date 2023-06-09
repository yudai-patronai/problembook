#!/usr/bin/env python3

import os
from lib import random
import shutil


def make_test(test_file, roman, answer):
    
    with open(test_file, 'w') as f:
        f.write(str(roman) + '\n')
    
    
    with open(test_file + '.a', 'w') as f:
        f.write(str(answer) + '\n')

if __name__ == '__main__':
    
    test_folder = 'tests'
    shutil.rmtree(test_folder, ignore_errors=True)
    os.mkdir(test_folder)
    
    boards_ans = {
        '01' : ('I', '1'),
        '02' : ('IV', '4'),
        '03' : ('IX', '9'),
        '04' : ('XIX', '19'),
        '05' : ('XXI', '21'),
        '06' : ('XXVI', '26'),
        '07' : ('XXXIII', '33'),
        '08' : ('XXXIV', '34'),
        '09' : ('XC', '90'),
        '10' : ('LXXXIV', '84'),
        '11' : ('LI', '51'),
        '12' : ('MCMXLVII', '1947'),
        '13' : ('MCMLXVIII', '1968'),
        '14' : ('MMXXXVIII', '2038'),
        '15' : ('MCMXCIX', '1999'),                              
        '16' : ('MCMLXXXIV', '1984'),
        '17' : ('CXLIX', '149'),
        '18' : ('C', '100')
    }
    
    for key, value in boards_ans.items():
        make_test(os.path.join(test_folder, key), value[0], value[1])

