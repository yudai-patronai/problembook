#!/usr/bin/python3

import os
import shutil

test_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

# https://en.wikipedia.org/wiki/List_of_prime_numbers
primes = [ (8, 19), (10, 29), (20, 71), (101, 547), (270, 1733), ]

for i, posp in enumerate(primes):
    i += 1
    pos, p = posp

    with open(os.path.join(test_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{}\n".format(pos))
    
    with open(os.path.join(test_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write("{}\n".format(p))