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


def solve(a, m):
    g, xg, _ = ext_euclid(a, m)
    if g != 1:
        return "No solution"
    return "{}".format(xg % m)


def get_case(a, m):
    return '{} {}'.format(a, m) + '\n', \
        solve(a, m) + '\n'


tests = TestSet()

tests.add(*get_case(5, 3))
tests.add(*get_case(4, 6))
tests.add(*get_case(3, 5))
tests.add(*get_case(4, 1))
tests.add(*get_case(0, 3))

for _ in range(RAND_TESTS_NUM):
    a = randint(-MAX_RAND_NUM, MAX_RAND_NUM)
    m = randint(2, MAX_RAND_NUM)
    tests.add(*get_case(a, m))
