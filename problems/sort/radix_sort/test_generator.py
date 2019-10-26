#!/usr/bin/python3
import os
import shutil
from lib import random
NUM_TEST = 10
random.seed(10000)

test_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

for i in range(1, NUM_TEST + 1):
    n = random.randint(1, 10)
    array = [random.randint(0, 16) for _ in range(n)]
    with open(os.path.join(test_dir, '{0:0>2}'.format(i)), 'w') as f:
        f.write('{0}\n'.format(' '.join(bin(val)[2:] for val in array)))

    with open(os.path.join(test_dir, '{0:0>2}.a'.format(i)), 'w') as f:
        n = len(array)
        maxx = max(array)
        p = 0
        while maxx > 0:
            p+=1
            maxx//=2
        for i in range(p):
            zero = []
            one =[]
            for j in range(n):
                if (array[j] % 2**(i+1)) // 2**(i) ==1:
                    one.append(array[j])
                else:
                    zero.append(array[j])
            array = zero + one
            strin = bin(array[0])[2:]
            for i in range(1,len(array)):
                strin += ' '+bin(array[i])[2:]
            strin +='\n'
            f.write(strin)
