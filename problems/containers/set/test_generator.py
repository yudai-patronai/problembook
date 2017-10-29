from lib.testgen import TestSet
from lib import random

MAX_RAND_TESTS = 10
RAND_TEST_SIZE = 100

def get_case():

	l = random.randint(1, 100)
	arr = [random.randint(100) for i in range(l)]
	q_str = '{}\n{}'.format(l, ' '.join(str(val) for val in arr))

	ret = len(set(arr))
	a_str = '{0}'.format(ret);
	return q_str, a_str

tests = TestSet()

for _ in range(MAX_RAND_TESTS):
	tests.add(*get_case())