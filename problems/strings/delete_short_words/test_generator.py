#!/usr/bin/env python3

import os
from lib import random
import shutil
import string

ALPHABET = list(string.ascii_letters)
NUM_TEST = 50

def generate_random_string(n):
    s = []
    for i in range(n):
        s.append(random.choice(ALPHABET))

    return "".join(s)

def generate_test_pair():
    sentence = ''
    answer = ''
    word_count = random.randint(42)
    for i in range(word_count):
        length = random.randint(8)
        word = generate_random_string(length)
        sentence += word
        if length > 3:
            answer += word

        if i != word_count - 1:
            sentence += ' '
            answer += ' '
    return (sentence, answer)

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
        ['Hello world', 'Hello world'],
        ['Mary had a little lamb','Mary   little lamb'],
        ['aaa bb c','  ']
    ]
    for n in range(len(tests) + 1, NUM_TEST + 1):
        tests.append(generate_test_pair())

    for i, t in enumerate(tests):
        generate_test(i + 1, t[0], t[1])

