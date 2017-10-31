from lib.testgen import TestSet
from lib.random import choice
from string import ascii_letters

NUM_RAND_TESTS = 20
MAX_TEST_SIZE = 1000


def get_case(words):
	d = {}
	for w in words:
		d.setdefault(w.lower(), 0)
		d[w.lower()] += 1


	word, freq = max(d.items(), key=lambda p: p[1])
	# There should be only one possible solution
	words.append(word)
	freq += 1

	q_str = '{}\n{}'.format(len(words), '\n'.join(words))
	a_str = '{} {}'.format(word, freq)

	return q_str, a_str


tests = TestSet()

tests.add(*get_case(['AaA']))
tests.add(*get_case(['AaA', 'aAa', 'AAA', 'AAA']))
tests.add(*get_case(['AaA', 'aAaA', 'AaAaA', 'aaaAAA']))

for _ in range(NUM_RAND_TESTS):
	words = [''.join(choice('AaBbCcDd') for _ in range(4)) for _ in range(MAX_TEST_SIZE)]
	tests.add(*get_case(words))
