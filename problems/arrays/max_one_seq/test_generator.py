import os
import shutil
from lib import random
# import random
import solution


def make_seq(N):
    seq = [random.randint(0, 1) for _ in range(N)]
    return seq


random.seed(228)
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

tests = [
    [1, [0], 0],
    [5, [1, 0, 1, 1, 0], 2],
    [4, [1, 1, 1, 1], 4],
    [6, [0, 0, 0, 0, 0, 0], 0]
]

simple_tests = 5
for num in range(simple_tests):
    N = random.randint(10, 40)
    seq = make_seq(N)
    ans = solution.solve(N, seq)
    tests.append([N, seq, ans])

hard_tests = 3
for num in range(hard_tests):
    N = random.randint(1000, 10000)
    seq = make_seq(N)
    ans = solution.solve(N, seq)
    tests.append([N, seq, ans])

for i, test in enumerate(tests):
    N, seq, ans = test
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(i + 1)), 'w') as f:
        f.write(str(ans))
    with open(os.path.join(tests_dir, '{0:0>2}'.format(i + 1)), 'w') as f:
        f.write('\n'.join(map(str, [N] + seq)))
