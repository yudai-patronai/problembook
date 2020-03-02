from lib.testgen import TestSet
from random import randint
from math import sqrt

def solution(x1, y1, r1, x2, y2, r2):
    r = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if r1 + r2 >= r and r + r2 >= r1 and r + r1 >= r2:
        return 'YES'
    return 'NO'

tests = TestSet()
tests.add('0 0 2\n0 3 2', 'YES\n')
tests.add('1 1 1\n4 4 1', 'NO\n')
for i in range(20):
    x2 = randint(0, 12)
    y2 = randint(0, 12)
    in_data = '4 4 4\n{} {} 1'.format(x2, y2) + '\n'
    out_data = solution(4, 4, 4, x2, y2, 1) + '\n'
    tests.add(in_data, out_data)

