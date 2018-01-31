import os
import shutil
#from lib 
import random
import string


def solution(seq):
    Composition = 0
    triple_sum = 0
    for index, value in enumerate(seq):
        triple_sum += value
        if (index + 1) % 3 == 0:
            Composition += (triple_sum % value)
            triple_sum = 0
    return [round(sum(seq) / len(seq), 3), max(seq), min(seq), Composition]


N = 5
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = list(range(1, 7))

    elif num == 2:
        seq = list(range(1, 10))
    
    elif num == 3:
        seq = [random.randint(1, 101) for _ in range(10 * 3)]

    elif num == 4:
        seq = [random.randint(1, 101) for _ in range(100 * 3)]
    
    elif num == 5:
        seq = [random.randint(1, 101) for _ in range(1000 * 3)]

    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write('\n'.join(list(map(str, seq)) + ['#']))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(' '.join(map(str, solution(seq))))
