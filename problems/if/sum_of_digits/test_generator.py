#!/usr/bin/python3

from lib import random
from lib.testgen import TestSet

random.seed(33)


tests = TestSet()
for i in range(10):
    num = random.randint(100, 999)
    ans = num // 100 + (num % 100) // 10 + num % 10

    tests.add(
        str(num) + '\n',
        str(ans) + '\n'
    )
