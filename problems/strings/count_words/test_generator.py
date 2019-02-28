#!/usr/bin/env python3

import os
from lib import random
import shutil
import string

ALPHABET = list(string.ascii_letters)
NUM_TEST = 15

def generate_random_string(n):
    s = []
    for i in range(n):
        s.append(random.choice(ALPHABET))

    return "".join(s)


def generate_test(i, answer):
    words = []

    for n in range(answer):
        words.append(generate_random_string(random.randint(42)))

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as fin:
        fin.write('{}\n'.format(' '.join(words)))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as fout:
        fout.write(str(answer)+'\n')

if __name__ == "__main__":
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    tests = [
        1,
        2,
        3
    ]
    for n in range(len(tests) + 1, NUM_TEST + 1):
        tests.append(random.randint(256))

    for i, t in enumerate(tests):
        generate_test(i + 1, t)
