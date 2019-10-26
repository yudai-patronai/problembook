from lib.testgen import TestSet
from lib.random import randint, randrange
from copy import copy

RAND_TESTS_NUM = 20
MAX_RAND_NUM = 1000
MAX_RAND_RANGE = 10

def cycle_shift_N(arr, N, M):
    M = M % N
    for i in range(M):
        tmp = arr[0]
        for idx in range(1, N):
            arr[idx - 1] = arr[idx]
        arr[-1] = tmp

def get_case(arr, N, M):
  arr_orig = copy(arr)
  cycle_shift_N(arr, N, M)
  return str(N) + '\n' + str(M) + '\n' + ' '.join(map(str, arr_orig)), ' '.join(map(str, arr))

tests = TestSet()

tests.add(*get_case([1, 2, 3, 4, 5], 5, 3))
tests.add(*get_case([1], 1, 10))

for _ in range(RAND_TESTS_NUM):
  N = randrange(1, MAX_RAND_RANGE)
  arr = [randint(MAX_RAND_NUM) for _ in range(N)]
  M = randrange(MAX_RAND_RANGE)
  tests.add(*get_case(arr, N, M))