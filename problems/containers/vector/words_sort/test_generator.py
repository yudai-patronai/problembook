from lib.testgen import TestSet
from lib.random import sample
from string import ascii_letters

MAX_RAND_TESTS = 20
RAND_TEST_SIZE = 100

def get_case(words):
	q_str = '{}\n{}'.format(len(words), ' '.join(words))

	ans_words = {w.lower() for w in words}
	a_str = ' '.join(sorted(ans_words, reverse=True))
	return q_str, a_str


tests = TestSet()

tests.add(*get_case(['AAA']))
tests.add(*get_case(['Aaaa', 'aAaA', 'AaAA']))
tests.add(*get_case(['Ab', 'Cd', 'Ba', 'Dc', 'Ab', 'Cd', 'Ba', 'Dc']))

for _ in range(MAX_RAND_TESTS):
	words = [''.join(sample(ascii_letters, 4)) for _ in range(RAND_TEST_SIZE)]
	tests.add(*get_case(words))
