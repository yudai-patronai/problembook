from lib.testgen import TestSet
from lib import random
from solution import solution

N = 8
random.seed(1984)

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


tests = TestSet()

for test_i in range(1, N + 1):
    if test_i == 1:
        n = 5
        A = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1],
             [1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]

    elif test_i == 2:
        n = 5
        A = generate_array(n, 0, 0)

    elif test_i == 3:
        n = 7
        A = generate_array(n, 2, 5)
    
    else:
        n = random.randint(7, 30)
        A = generate_array(n, random.randint(1, n), random.randint(1, n))
    
    question = str(n) + '\n'
    question += '\n'.join( [' '.join(map(str, row)) for row in A] )
    question += '\n'
    
    stok, istok = solution(n, A)
    answer = ' '.join(map(str, istok)) + '\n'
    answer += ' '.join(map(str, stok)) + '\n'

    tests.add(question, answer)
