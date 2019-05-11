import os
import shutil
from lib import random


N = 8
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)


def solution(n, A):
    istok = []
    stok = []

    for i in range(n):
        if sum(A[i]) == 0:
            stok.append(i+1)
    stok.sort()
    
    for i in range(n):
        if sum([sub_list[i] for sub_list in A]) == 0:
            istok.append(i+1)
    istok.sort()
    
    return ' '.join(map(str, istok)), ' '.join(map(str, stok))


def generate_array(n, istok, stok):
    A = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]

    istok_seq = random.sample(range(n), istok)
    stok_seq = random.sample(range(n), stok)

    for i in istok_seq:
        A[i] = [0]*n

    for i in stok_seq:
        for sub_list in A:
            sub_list[i] = 0

    return A


for num in range(1, N + 1):
    if num == 1:
        n = 5
        A = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    elif num == 2:
        n = 5
        A = generate_array(n, 0, 0)

    elif num == 3:
        n = 7
        A = generate_array(n, 2, 5)
    
    else:
        n = random.randint(7, 30)
        A = generate_array(n, random.randint(1, n), random.randint(1, n))
    
    
    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(str(n) + '\n')
        f.write('\n'.join([' '.join(map(str, sub_list)) for sub_list in A]))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        answer = solution(n, A)
        f.write('\n'.join(answer))