#!/usr/bin/python3

import os
import shutil
import random
#from lib import random

N = 50;
random.seed(10000)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i in range(1, N + 1):
    x = random.randrange(1,5000)

    temp = x
    ret = 0;
    while temp != 0:
        if temp % 2 == 1:
            if temp == 1:
                break
            ret += 1
            temp -= 1
            continue
        ret += 1
        temp = temp / 2

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write("{0}\n".format(x))
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        f.write(format(ret))
