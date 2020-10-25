from lib.testgen import TestSet
from lib.random import seed, randint


seed(42)
MAX_INT = 1_000_000


def array2str(A, end='\n'):
    return ' '.join(map(str, A)) + end


def sort_evens(A:list):
    evens = sorted(filter(lambda x: x % 2 == 0, A))
    ei = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[i] = evens[ei]
            ei += 1


tests = TestSet()
manual_qa = [
    (
        [8, 1, 6, 7, 1],    # question
        [6, 1, 8, 7, 1],    # answer
    ),
    (
        [1, 7, 8, 2, 6, 7, 9, 10, 4, 3],
        [1, 7, 2, 4, 6, 7, 9, 8, 10, 3],
    ),
    (
        [2, -1, 6, -5, 8, 3, 0],
        [0, -1, 2, -5, 6, 3, 8]
    )
]   

for qA, aA in manual_qa:
    tests.add(array2str(qA), array2str(aA))

for _ in range(5):
    A = [randint(-MAX_INT, MAX_INT) for _ in range(randint(10, 50))]
    q = array2str(A)
    sort_evens(A)
    a = array2str(A)
    tests.add(q, a)

# все нечётные
A = [ (2*randint(0, MAX_INT)+1) % MAX_INT for _ in range(20)]
tests.add(array2str(A), array2str(A))

# все чётные
A = [ (2*randint(0, MAX_INT)) % MAX_INT for _ in range(20)]
tests.add(array2str(A), array2str(sorted(A)))
