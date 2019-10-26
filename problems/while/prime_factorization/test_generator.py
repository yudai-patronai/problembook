#!/usr/bin/python3

import os
import shutil

test_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

def prime_factorization(n):
    factor = 2
    factors = []
    while n * n > factor + 1:
        if n % factor == 0:
            n //= factor
            factors.append(str(factor))
        else:
            factor += 1
    return "\n".join(factors)

numbers = [265, 271828, 314159265, 29832, 24095, 7463920]

for test_num, question in enumerate(numbers):
    test_num += 1
    
    answer = prime_factorization(question)

    with open(os.path.join(test_dir, '{0:0>2}'.format(test_num)), 'w') as f:
        f.write("{}\n".format(question))
    
    with open(os.path.join(test_dir, '{0:0>2}.a'.format(test_num)), 'w') as f:
        f.write("{}\n".format(answer))