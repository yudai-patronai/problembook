from lib.testgen import TestSet
from lib.random import randint, randrange
from copy import copy

RAND_TESTS_NUM = 20
MAX_RAND_NUM = 1000
MAX_RAND_RANGE = 100

def cycle_shift_N(arr, N, M):
    tmp = arr[0]
    for i in range(0,  M * (N - 1), M):
        arr[i % N] = arr[(i + M) % N]
    arr[M * (N-1) % N] = tmp

def get_case(arr, N, M):
  arr_orig = copy(arr)
  cycle_shift_N(arr, N, M)
  return str(N) + '\n' + str(M) + '\n' + ' '.join(map(str, arr_orig)), ' '.join(map(str, arr))

tests = TestSet()

tests.add(*get_case([1, 2, 3, 4, 5], 5, 3))
tests.add(*get_case([1], 1, 10))

for _ in range(RAND_TESTS_NUM):
  N = randrange(MAX_RAND_RANGE)
  arr = [randint(MAX_RAND_NUM) for _ in range(N)]
  M = randrange(MAX_RAND_RANGE)
  tests.add(*get_case(arr, N, M))