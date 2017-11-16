import os
import shutil
from lib import random

def solution(seq):
    arr = sorted(seq)
    N = len(arr)

    weight = [float('Inf'), arr[1] - arr[0]]
    for i in range(2, N):
        weight.append(min(weight[i - 1], weight[i - 2]) + (arr[i] - arr[i - 1]))
    return(weight[-1])



N = 6
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = [4, 10, 0, 12, 2]
    elif num == 2:
        seq = [3, 4, 12, 6, 14, 13]
    elif num == 3:
        seq = [2, 3]
    elif num == 4:
        seq = random.sample(range(1, 10000), 6)
    else:
        seq = random.sample(range(1, 10000), 100)
    
    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(" ".join(map(str, seq)))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(str(solution(seq)))
