from lib.testgen import TestSet
from lib.random import randint

RAND_TESTS_NUM = 5
MAX_RAND_NUM = 100000


def ext_euclid(a, b):
    x = 1
    y = 0
    qs = []
    while b != 0:
        q, r = divmod(a, b)
        qs.append(q)
        a, b = b, r
    for q in reversed(qs):
        x, y = y, x - y * q
    return a, x, y

def solve_modulo_eq(m, a, b):
    if a < 0:
        b = -b
        a = -a
    g, x0, k0 = ext_euclid(a, m)
    if b % g != 0:
        return False
    dx = m // g
    x1 = x0 * (b // g)
    solutions = [x1 % m]
    for k in range(1, g):
        xk = solutions[k - 1] + dx
        solutions.append(xk % m)
    return sorted(solutions)


tests = TestSet()

def add(m, a, b):
    question = '{}\n{}\n{}\n'.format(m, a, b)
    sol = solve_modulo_eq(m, a, b)
    if not sol:
        answer = '-1\n'
    else:
        answer = ' '.join(sol) + '\n'
    tests.add(question, answer)


add(3, 2, 1)
add(26, 8, 7)
add(1, 2, 33)
add(1, 2, 34)
add(18, 12, 6)

for _ in range(RAND_TESTS_NUM // 2):
    m = randint(2, MAX_RAND_NUM)
    a = randint(-MAX_RAND_NUM, MAX_RAND_NUM)
    b = randint(-MAX_RAND_NUM, MAX_RAND_NUM)
    add(m, a, b)
