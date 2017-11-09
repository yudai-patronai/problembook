#!/usr/bin/python3

from lib.random import choice, randint
from string import ascii_letters
from lib.testgen import TestSet

NUM_TEST = 10
MAX_STR_LEN = 256
ALPHABET = ascii_letters + ' '

def get_case(instr):
    return instr, instr[::-1]

tests = TestSet()

tests.add(*get_case('AAAAA'))
tests.add(*get_case('    '))
tests.add(*get_case('a a '))

for _ in range(NUM_TEST):
    instr = ''.join(choice(ALPHABET) for _ in range(randint(42, MAX_STR_LEN)))
    tests.add(*get_case(instr))
