from lib.testgen import TestSet
from lib.random import randint

RAND_TESTS_NUM = 4
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


def solve(a, b, c, x_min, x_max, y_min, y_max):
    if a == 0 and b == 0:
        if c == 0:
            return str((x_max - x_min + 1) * (y_max - y_min + 1))
        else:
            return "0"
    g, xg, yg = ext_euclid(a, b)
    if c % g != 0:
        return "0"
    x0 = xg * c // g
    y0 = yg * c // g

    kx_min = (x_min - x0) * g // b
    kx_max = (x_max - x0) * g // b
    ky_min = (y0 - y_max) * g // a
    ky_max = (y0 - y_min) * g // a

    if kx_min > ky_max or kx_max < ky_min:
        return "0"
    if ky_min <= kx_min <= ky_max:
        return str(min(ky_max, kx_max) - kx_min + 1)
    else:
        return str(min(ky_max, kx_max) - ky_min + 1)


def get_case(a, b, c, d, e, f, g):
    return '{} {} {}\n{} {}\n{} {}\n'.format(a, b, c, d, e, f, g), \
        solve(a, b, c, d, e, f, g) + '\n'


tests = TestSet()

tests.add(*get_case(1, 2, 3, -5, 5, -5, 5))
tests.add(*get_case(10, 6, 8, 0, 10, 2, 6))
tests.add(*get_case(0, 0, 3, -5, 3, -2, 6))
tests.add(*get_case(5, 5, 0, 0, 2, 8, 14))
tests.add(*get_case(0, 0, 0, 0, 5, -5, 0))
tests.add(*get_case(1, 2, 3, -3, -3, 3, 3))

for _ in range(RAND_TESTS_NUM):
    a = randint(MAX_RAND_NUM)
    b = randint(MAX_RAND_NUM)
    g, _, _ = ext_euclid(a, b)
    c = randint(MAX_RAND_NUM // g)
    x_min = randint(-10**9, 10**9)
    x_max = randint(-10**9, 10**9)
    y_min = randint(-10**9, 10**9)
    y_max = randint(-10**9, 10**9)
    tests.add(*get_case(a, b, c * g, x_min, x_max, y_min, y_max))
    tests.add(*get_case(a, b, g * c + a % c, x_min, x_max, y_min, y_max))
