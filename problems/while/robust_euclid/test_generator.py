from lib.testgen import TestSet
from lib.random import randint

RAND_TESTS_NUM = 5
MAX_RAND_NUM = 10 ** 9

def robust_euclid(a, b):
  while b != 0:
    r = a % b
    a = b
    b = r
  return abs(a)

def get_case(a, b):
  d = robust_euclid(a, b)
  return '{} {}'.format(a, b), str(d)

tests = TestSet()

tests.add(*get_case(-5, -15))
tests.add(*get_case(5, -15))
tests.add(*get_case(-5, 15))
tests.add(*get_case(0, 10))
tests.add(*get_case(10, 0))

for _ in range(RAND_TESTS_NUM):
  a = randint(MAX_RAND_NUM)
  b = randint(MAX_RAND_NUM)
  tests.add(*get_case(a, a * 2**10))
  tests.add(*get_case(a * 3**5 * 2**4, a))
  tests.add(*get_case(a*b, b))
  tests.add(*get_case(a, b*a))

