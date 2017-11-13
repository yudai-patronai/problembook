#!/usr/bin/env python3
from lib.testgen import TestSet
from lib.random import randint

MAX_RAND_TESTS = 20

def get_case(seq):
    question = ' '.join(str(a) for a in seq)
    answer = '.'.join([str(x) for x in seq])
    return question, answer

def get_seq():
    day = randint(1,30)
    month = randint(1, 12)
    year = randint(1, 3000)
    sequense = [day,month,year]
    return sequense

tests = TestSet()

for _ in range(MAX_RAND_TESTS):
    tests.add(*get_case(get_seq()))
