import os
import shutil

from lib import random


N = 50
TEST_PATH = "tests"


def get_random_matrix():
	N = random.randint(1, 10)
	lines = [[random.randint(0, 1000) for _ in range(N)] for _ in range(N)]
	trace = sum(line[i] for (i, line) in enumerate(lines))
	lines = [str(N)] + [" ".join(map(str, line)) for line in lines]

	return lines, trace

def main():
	shutil.rmtree(TEST_PATH, ignore_errors=True)
	os.mkdir(TEST_PATH)

	for i in range(N):
		matrix, trace = get_random_matrix()
		with open(os.path.join(TEST_PATH, str(i)), "w") as f:
			f.write("\n".join(matrix))
		
		with open(os.path.join(TEST_PATH, str(i) + ".a"), "w") as f:
			f.write(str(trace))


if __name__ == "__main__":
	main()
