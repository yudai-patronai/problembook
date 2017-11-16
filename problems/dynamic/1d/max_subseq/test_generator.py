import os
import shutil
from lib import random

def solution(arr):
    N = len(arr)
    subseq_len = []
    for i in range(N):
        subseq = [el for index, el in enumerate(subseq_len) if arr[index] < arr[i]]
        if subseq:
            subseq_len.append(max(subseq) + 1)
        else:
            subseq_len.append(1)
    return max(subseq_len)



N = 10
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = [3, 29, 5, 5, 28, 6]
    elif num == 2:
        seq = [1]
    elif num == 3:
        seq = [5, 4, 3, 2, 1]
    elif num == 4:
        seq = [1, 1, 1, 1, 1]
    elif num == 5:
        seq = random.sample(range(1, 10000), 6)
    else:
        seq = random.sample(range(1, 10000), 100)
    
    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(" ".join(map(str, seq)))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(str(solution(seq)))
