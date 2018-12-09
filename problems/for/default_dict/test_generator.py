#!/usr/bin/env python3

import os
# from lib import random
# import random
import shutil

def generate_test(i, original, answer):

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as fin:
        fin.write(original)

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as fout:
        fout.write(answer)

if __name__ == "__main__":
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    tests = [
        ['Hi, this is Bob!', 'Hi this is Bob!'],
        ["My phone is +44_555_5555555. Don't forget to call me!",
        'My phone is +FOURFOUR']
    ]

    inputs = ['1 0 0 1 123 4',
     '0 0 0 1 123 4',
     '1 7 7 7 8 8 8 8 8',
     '1 0 1 2 3 4 5',
     '1 1 2 3 4 5 4 3 2 1',
     '0 1 1 2 2 3 3',
     '1 1 1 2 2 3 3']

    answers = ['>>1>>>>1>>>>2>>>>3>>>>4>>',
     '',
     '>>1>>>>1>>>>1>>>>2>>>>2>>>>2>>>>2>>>>2>>',
     '>>1>>>>2>>>>3>>>>4>>>>5>>>>6>>',
     '>>1>>>>2>>>>3>>>>4>>>>5>>>>4>>>>3>>>>2>>>>1>>',
     '',
     '>>1>>>>1>>>>2>>>>2>>>>3>>>>3>>']

    for i, t in enumerate(zip(inputs, answers)):
        generate_test(i + 1, t[0], t[1])



