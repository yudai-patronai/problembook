from lib.testgen import TestSet
from lib.random import randint

RAND_TESTS_NUM = 5
MAX_RAND_NUM = 10 ** 9

def get_case(num):
	ans = 'YES' if num & (num - 1) == 0 else 'NO'
	return str(num), ans

tests = TestSet()

tests.add(*get_case(1))
tests.add(*get_case(2))
tests.add(*get_case(3))
tests.add(*get_case(4))
tests.add(*get_case(5))

tests.add(*get_case(2 ** 10))
tests.add(*get_case(2 ** 12))
tests.add(*get_case(2 ** 16))

for _ in range(RAND_TESTS_NUM):
	tests.add(*get_case(randint(MAX_RAND_NUM)))
