from lib import random
from lib.testgen import TestSet

N = 50

def get_random_matrix():
    N = random.randint(1, 10)
    lines = [[random.randint(0, 1000) for _ in range(N)] for _ in range(N)]
    trace = sum(line[i] for (i, line) in enumerate(lines))
    lines = [str(N)] + [" ".join(map(str, line)) for line in lines]

    return lines, trace

def main():
    tests = TestSet()

    for i in range(N):
        matrix, trace = get_random_matrix()
        tests.add("\n".join(matrix) + "\n", str(trace) + '\n')


if __name__ == "__main__":
    main()
