#!/usr/bin/env python3

import os
from lib import random
# import random
import shutil
import string
import solution

random.seed(1984)

ALPHABET = list(string.ascii_letters + string.digits + ',.-_ ')

NUM_TEST = 20

def generate_random_string(n):
    s = []
    for i in range(n):
        s.append(random.choice(ALPHABET))

    return "".join(s)

def generate_test_pair():
    sentence = ''
    answer = ''
    word_count = random.randint(50) + 1
    for i in range(word_count):
        length = random.randint(20) + 1
        word = generate_random_string(length)
        sentence += word + '\n'

    if random.randint(10) % 2:
        sentence += word
    # else:
    #     sentence += '\n'

    answer = solution.generate_answer(sentence)
    return (sentence, answer)

def generate_test(i, original, answer):

    with open(os.path.join(tests_dir, '{0:0>2}'.format(i)), 'w') as fin:
        fin.write(original + "\n")

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i)), 'w') as fout:
        fout.write(answer)

if __name__ == "__main__":
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    tests = [
        ['Who is a good boy?\nmipt\n777\niddqd idkfa idclip\n- Good\n',
        'mt77ip-d'],
        ['a\nphystech2\nphystech2',
        'aap2']
    ]
    for n in range(len(tests) + 1, NUM_TEST + 1):
        tests.append(generate_test_pair())

    for i, t in enumerate(tests):
        generate_test(i + 1, t[0], t[1])



