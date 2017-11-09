from lib import random
from lib.testgen import TestSet
import string

TESTS_NUM = 10
ALPHABET = list(string.ascii_lowercase + string.ascii_uppercase + ' ')

def generate_random_string(n, alphabet):
	s = []
	for i in range(n):
		s.append(random.choice(alphabet))
	return "".join(s)

def formatString():

	start_str = generate_random_string(random.randint(10, 255), ALPHABET)
	end_str = ""
	ind = 0
	for j in start_str:
		if (j.isspace()):
			end_str += ' '
			continue

		end_str = ''.join((end_str, j.upper() if (ind % 2 == 0) else j.lower()))
		ind = ind + 1

	return start_str, end_str


if __name__ == "__main__":

	tests = TestSet()

	for _ in range(TESTS_NUM):
		tests.add(*formatString())