from lib.testgen import TestSet
from lib.random import randint

RAND_TESTS_NUM = 10
MAX_RAND_NUM = 1000

def ferma_small(p):
  if p == 1 or p == 2:
    return 'YES'
  else:
    N = 2 ** (p-1)
    if N % p == 1:
        return 'YES'
    else:
      return 'NO'

def get_case(a):
  return str(a) + '\n', ferma_small(a) + '\n'

tests = TestSet()

for i in range(1, 16):
  tests.add(*get_case(i))

for _ in range(RAND_TESTS_NUM):
  a = randint(MAX_RAND_NUM)
  tests.add(*get_case(a))


