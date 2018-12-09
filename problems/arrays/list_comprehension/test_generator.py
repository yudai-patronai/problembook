import os
import shutil
from lib import random
from collections import Counter

def solution(lst):
    return [x * 2 if x > 10 else x - 5 for x in lst if x != 3]

def make_seq(n_three, n_other):
    left = [3] * n_three
    right = [random.randint(0, 99) for _ in range(n_other)]
    out = left + right
    random.shuffle(out)
    return(out)

N = 5
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = [11, 3, 9]

    elif num == 2:
        seq = [5, 5, 5]
    
    elif num == 3:
        seq = make_seq(3, 10)
    
    else:
        seq = make_seq(10, 50)

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(' '.join(map(str, solution(seq))))

    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(' '.join(map(str,seq)))

