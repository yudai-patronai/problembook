import os
import shutil
# from lib 
import random
from collections import Counter
from itertools import product

MENS_RAW = ['Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'George', 'Oscar', 'James', 'William']
MENS = [x + 'm' for x in MENS_RAW]

WOMENS_RAW = ['Amelia', 'Olivia', 'Isla', 'Emily', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Lily', 'Sophie']
WOMENS = [x + 'w' for x in WOMENS_RAW]

def solution(lst):
    men = [x for x in lst if x[-1] == 'm']
    women = [x for x in lst if x[-1] == 'w']

    pairs = ['{}_{}'.format(x, y) for x, y in product(men, women)]
    pairs.sort()
    return pairs


def make_seq(n_m, n_w):
    out = random.sample(MENS, n_m) + random.sample(WOMENS, n_w)
    random.shuffle(out)
    return(out)

N = 5
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = make_seq(1, 2)

    elif num == 2:
        seq = make_seq(2, 2)
    
    elif num == 3:
        seq = make_seq(3, 4)
    
    else:
        seq = make_seq(7, 7)

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write('\n'.join(map(str, solution(seq))))

    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(' '.join(map(str,seq)))

