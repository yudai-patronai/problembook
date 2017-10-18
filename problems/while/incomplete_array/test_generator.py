#!/usr/bin/python3

import os
from lib import random
import shutil
import sys

NUM_RANDOM_TEST = 5
    
manual = {
    "case" : [
        [1,2,3,4,5,6],
        [2,2,2,2,2,2],
        [6,7,5,4,4,3,2,1,5],
        [1,2,3,4,5,6,5,4,3,2,1],
        [1,10000,10000,10000,10000,10000]
    ],
    "answer" : [
        1,
        2,
        7,
        6,
        1
    ]
}

random.seed(42)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for i, (case, answer) in enumerate(zip(manual["case"], manual["answer"])):
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i+1)), 'w') as fin:
        fin.write("\n".join(map(str, case + [0])))
    
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i+1)), 'w') as fout:
        fout.write(str(answer))

shift = len(manual["answer"])
for i in range(shift+1, shift+NUM_RANDOM_TEST+1):
    mx = [0]*6
    cur = -1
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as fin:
        for strnum in range(1000000 if i == 10 else random.randint(6,1000)):
            cur = (cur+1)%6
            elem = random.randint(1,1000000000) 
            mx[cur] = max(mx[cur-1], elem)
            fin.write("{}\n".format(elem))
        fin.write("0")

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as fout:
        fout.write('{}'.format(mx[(cur+1)%6]))
