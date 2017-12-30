from lib.random import randint
from lib.testgen import TestSet

MAX_RAND_TESTS = 20
MAX_RAND_TEST_SIZE = 100

def get_case(values):
	q_str = '{}\n{}\n'.format(len(values), '\n'.join(map(str, values)))

	ans = sorted([(v, values.count(v)) for v in set(values)])
	a_str = '\n'.join('{} {}'.format(*a) for a in ans)

	return q_str, a_str

tests = TestSet()

tests.add(*get_case([1]))
tests.add(*get_case([1, 1, 1, 1, 1]))
tests.add(*get_case([1, 2, 3, 4, 5]))

for _ in range(MAX_RAND_TESTS):
	values = [randint(1, sz // 2) for sz in range(randint(10, MAX_RAND_TEST_SIZE))]
	tests.add(*get_case(values))
