import os
import shutil
from lib import random
import string


def solution(seq):
    average = sum(seq) / len(seq)
    return sum(list(filter(lambda x: x > average, seq)))


def generate_seq(n, min_, max_):
    return [random.randint(min_, max_) for _ in range(n)]

N = 6
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = [1, 2, 3, 4, 5]

    elif num == 2:
        seq = generate_seq(3, 1, 1)

    
    elif num == 3:
        seq = generate_seq(1, 1, 1)

    elif num == 4:
        seq = generate_seq(30, 0, 100)
    
    else:
        seq = generate_seq(300, 0, 100)

    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write('\n'.join(map(str, [len(seq)] + seq)))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(str(solution(seq)))
