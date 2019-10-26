#!/usr/bin/python3

import os
import shutil

test_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)


def factorial_trailing_zeros(n):
    pow_of_5 = 5
    zeros = 0
    
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
        
    return zeros

numbers = [ 8, 30, 72, 250, 450, 1000, 12000, 15000 ]

for test_ord, question in enumerate(numbers):
    test_ord += 1
    
    answer = factorial_trailing_zeros(question)

    with open(os.path.join(test_dir, '{0:0>2}'.format(test_ord)), 'w') as f:
        f.write("{}\n".format(question))
    
    with open(os.path.join(test_dir, '{0:0>2}.a'.format(test_ord)), 'w') as f:
        f.write("{}\n".format(answer))