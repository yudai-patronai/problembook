from lib.testgen import TestSet
from lib.random import sample

MAX_RAND_NUM = 100

def get_case(num):
	ans = '1' if num % 3 == 1 or num % 3 == 2 else '2'
	return str(num), ans

tests = TestSet()

tests.add(*get_case(1))
tests.add(*get_case(2))
tests.add(*get_case(3))
tests.add(*get_case(4))
tests.add(*get_case(5))
tests.add(*get_case(6))

s = sample(range(7, 100), 24)

for i in s:
	tests.add(*get_case(i))
