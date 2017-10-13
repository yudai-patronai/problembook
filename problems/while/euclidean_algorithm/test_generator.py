#!/usr/bin/python3

import os
import shutil

from lib import random
N = 15
random.seed(10000)

test_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

def eucl_alg(firstNumber, secondNumber):
    while firstNumber != secondNumber:
        if firstNumber > secondNumber:
            firstNumber -= secondNumber
        else:
            secondNumber -= firstNumber

    return firstNumber



for i in range(1, N + 1):
    if i == 1:
        x1 = 15
        x2 = 1
    else:
        x1 = random.randrange(1, 10000)
        x2 = random.randrange(1, 10000)

    with open(os.path.join(test_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0}\n{1}\n".format(x1, x2))
    with open(os.path.join(test_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(format(eucl_alg(x1, x2)))
