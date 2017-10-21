#!/usr/bin/python3

import os
from lib import random
import shutil
from string import ascii_lowercase
from lib.testgen import TestSet

NUM_RAND_TEST = 10
MAX_STR_LEN = 256

random.seed(42)

def get_case(text):
    return (text, text.lower())

tests = TestSet()

for _ in range(NUM_RAND_TEST):
    # use random.choice instead of random.smaple cause MAX_STR_LEN > len(ascii_lowercase)
    lower_chars = ''.join([random.choice(ascii_lowercase + ' ') for _ in range(random.randint(1, MAX_STR_LEN))])
    upper_chars = ''.join([c.upper() if hash(c) % 2 == 0 else c for c in lower_chars])
    tests.add(upper_chars, lower_chars)

# All lowercase tests
tests.add('testtesttest', 'testtesttest')
tests.add('test test test', 'test test test')

# All uppercase tests
tests.add('TESTTESTTEST', 'testtesttest')
tests.add('TEST TEST TEST', 'test test test')
