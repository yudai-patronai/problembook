from lib.testgen import TestSet
from lib.random import randint

RAND_TESTS_NUM = 5
MAX_RAND_NUM = 10 ** 9

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

def get_case(a, b):
    return '{} {}'.format(a, b) + '\n', '{} {} {}'.format(*ext_euclid(a, b)) + '\n'

tests = TestSet()

tests.add(*get_case(10, 36))
tests.add(*get_case(9, 11))
tests.add(*get_case(500, 305))
tests.add(*get_case(0, 10))
tests.add(*get_case(10, 0))

for _ in range(RAND_TESTS_NUM):
    a = randint(MAX_RAND_NUM)
    b = randint(MAX_RAND_NUM)
    tests.add(*get_case(a, a * 2**10))
    tests.add(*get_case(a * 3**5 * 2**4, a))
    tests.add(*get_case(a*b, b))
    tests.add(*get_case(a, b*a))

