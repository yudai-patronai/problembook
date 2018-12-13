import os
import shutil
from lib import random
from collections import Counter
from itertools import product, combinations, permutations

MENS_RAW = ['Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'George', 'Oscar', 'James', 'William']
MENS = [x + 'm' for x in MENS_RAW]

WOMENS_RAW = ['Amelia', 'Olivia', 'Isla', 'Emily', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Lily', 'Sophie']
WOMENS = [x + 'w' for x in WOMENS_RAW]

def grouper(seq, last, value):
    men = [x for x in seq if x[-1] == last]
    return ['+'.join(x) for x in permutations(men, value)]

def solution(names, p, q):
    men = grouper(names, 'm', p)
    women = grouper(names, 'w', q)

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
        p, q = 2, 1
        seq = make_seq(2, 1)

    elif num == 2:
        p, q = 2, 2
        seq = make_seq(2, 2)
    
    elif num == 3:
        p, q = 2, 2
        seq = make_seq(3, 3)
    
    else:
        p, q = random.randint(1, 3), random.randint(1, 3)
        seq = make_seq(p + random.randint(1, 2),  q + random.randint(1, 2))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write('\n'.join(map(str, solution(seq, p, q))))

    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(' '.join(map(str, [p, q])))
        f.write('\n')
        f.write(' '.join(map(str, seq)))

