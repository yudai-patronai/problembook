#!/usr/bin/python3

from lib import random
from lib.testgen import TestSet


tests = TestSet()
NUM_TEST = 9

YES = 'YES\n'
NO = 'NO\n'

random.seed(42)

def sol(N):
    count = 0
    while N > 0:
        count += N % 2
        N //= 2
    return not count

for i in range(6):
    tests.add('{}\n'.format(2 ** random.randint(0, 14)), YES)

for i in range(6, NUM_TEST - 1):
    test_num = random.randint(1, 10000)
    tests.add('{}\n'.format(test_num), YES if sol(test_num) else NO)

tests.add('1\n', YES)