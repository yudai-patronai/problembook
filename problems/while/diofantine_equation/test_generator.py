from lib.testgen import TestSet
from lib.random import randint

RAND_TESTS_NUM = 5
MAX_RAND_NUM = 10000


def ext_euclid(a, b):
    x = 1
    y = 0
    qs = []
    while b != 0:
        r = a % b
        q = a // b
        qs.append(q)
        a = b
        b = r
    for q in qs[::-1]:
        buf = y
        y = x - y * q
        x = buf
    return a, x, y


def solve(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            return "1 1"
        else:
            return "No solution"
    g, xg, yg = ext_euclid(a, b)
    if c % g != 0:
        return "No solution"
    return "{} {}".format(xg * c // g, yg * c // g)


def get_case(a, b, c):
    return '{} {} {}'.format(a, b, c) + '\n', \
        solve(a, b, c) + '\n'


tests = TestSet()

tests.add(*get_case(1, 2, 3))
tests.add(*get_case(10, 6, 8))
tests.add(*get_case(5, 5, 0))
tests.add(*get_case(0, 0, 0))
tests.add(*get_case(0, 0, 3))

for _ in range(RAND_TESTS_NUM):
    a = randint(MAX_RAND_NUM)
    b = randint(MAX_RAND_NUM)
    g, _, _ = ext_euclid(a, b)
    c = randint(MAX_RAND_NUM // g)
    tests.add(*get_case(a, b, c * g))
    tests.add(*get_case(a, b, g * c + a % c))
