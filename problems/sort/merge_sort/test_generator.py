from lib.testgen import TestSet
from lib.random import randint


NUMBER_OF_RANDOM_TESTS = 7
RANDOM_ARRAY_SIZE = 25
RANDOM_ARRAY_ELEMENT_MINMAX = (-100, 100)

LOG_VAR = ''  #  global var for store log messages

def question(A):
    return ' '.join(map(str, A)) + '\n'


def answer(A):
    return ' '.join(map(str, A)) + '\n'


def random_array(size):
    random_arr = [ randint(*RANDOM_ARRAY_ELEMENT_MINMAX) for _ in range(size)]
    return random_arr


def merge(L, R):
    len_L, len_R = len(L), len(R)
    
    A = [0] * (len_L + len_R)
    ind_L = ind_R = ind_A = 0
    
    while ind_L < len_L and ind_R < len_R:
        if L[ind_L] <= R[ind_R]:
            A[ind_A] = L[ind_L]
            ind_L += 1
            ind_A += 1
        else:
            A[ind_A] = R[ind_R]
            ind_R += 1
            ind_A += 1
    
    while ind_L < len_L:
        A[ind_A] = L[ind_L]
        ind_A += 1
        ind_L += 1
    
    while ind_R < len_R:
        A[ind_A] = R[ind_R]
        ind_A += 1
        ind_R += 1
    
    return A


def merge_sort(A, depth=1, part='left', log=[]):
    log.append( 'depth: {:d} | part: {:s} | array: {}'.format(depth, part, A) )

    if len(A) <= 1:
        return

    middle = len(A) // 2
    L = A[:middle]
    R = A[middle:]
    merge_sort(L, depth + 1, 'left', log)
    merge_sort(R, depth + 1, 'right', log)
    C = merge(L, R)

    for i in range(len(A)):
        A[i] = C[i]

    log.append( 'depth: {:d} | part: {:s} | after merge: {}'.format(depth, part, A) )


tests = TestSet()

for arr in [2, 4, 8, 1, 2, 3, 10], [4, 3, 10], [2, 4, 8]:
    log = []
    q = question(arr)
    merge_sort(arr, log=log)

    tests.add(
        q,
        '\n'.join(log) + '\n'
    )

for _ in range(NUMBER_OF_RANDOM_TESTS):
    log = []
    random_A = random_array(RANDOM_ARRAY_SIZE)
    
    q = question(random_A)
    merge_sort(random_A, log=log)

    tests.add(
        q,
        '\n'.join(log) + '\n'
    )
