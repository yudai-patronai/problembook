from lib import random
from lib.testgen import TestSet


def insertion_sort_ans(A):
    ans = ' '.join(map(str, A)) + '\n'
    for i in range(1, len(A)):
        for j in range(i, 0, -1): 
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
                ans += ' '.join(map(str, A)) + '\n'
    return ans


NUM_TEST = 10
random.seed(10000)

tests = TestSet()

manual = [
    [-5, 3, 1, 7, 10, -4],
    [9, 2, 4, 2, 9, 5, -1, -8],
]

for A in manual:
    question = ' '.join(map(str, A)) + '\n'
    tests.add(question, insertion_sort_ans(A))

for i in range(NUM_TEST - len(manual)):
    A = [random.randint(-100, 100) for _ in range(random.randint(10, 20))]

    question = ' '.join(map(str, A)) + '\n'
    tests.add(question, insertion_sort_ans(A))
