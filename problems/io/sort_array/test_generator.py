from lib.testgen import TestSet
from lib import random

TESTS_NUM = 10

def sortArray():
	n = random.randint(1, 1000)
	array = []
	for j in range(n):
		array.append(random.randint(-1000, 1000))

	return '{}'.format(' '.join(str(val) for val in array)), '{}'.format(' '.join(str(val) for val in sorted(array)))


tests = TestSet()

for _ in range(TESTS_NUM):
	tests.add(*sortArray())