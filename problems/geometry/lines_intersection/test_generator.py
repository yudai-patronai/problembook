from lib.testgen import TestSet
from random import randint
from math import sqrt

def solution(a1, b1, c1, a2, b2, c2):
    eps = 1e-6
    d = a1 * b2 - b1 * a2
    if abs(d) < eps:
        return ['NO']
    x = (b1 * c2 - c1 * b2) / d
    y = -(c2 + a2 * x) / b2
    return [str(round(x)), str(round(y))]

tests = TestSet()
tests.add('1 -1 0\n2 -1 1', '-1 -1\n')
tests.add('1 2 3\n4 8 7', 'NO\n')
for i in range(10):
    a1 = randint(1, 10)
    b1 = randint(11, 20)
    c1 = randint(21, 30)
    a2 = randint(31, 40)
    b2 = randint(41, 50)
    c2 = randint(51, 60)
    in_data = '{} {} {}\n{} {} {}\n'.format(a1, b1, c1, a2, b2, c2)
    out_data = ' '.join(solution(a1, b1, c1, a2, b2, c2)) + '\n'
    tests.add(in_data, out_data)
