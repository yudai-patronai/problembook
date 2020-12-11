from lib.testgen import TestSet
from solution import transpose
from lib.random import randint, seed

seed(142)


def answer(A):
    s = ''
    for row in A:
        s += ' '.join(map(str, row)) + '\n'
    return s

def question(A):
    s = str(len(A)) + '\n' + answer(A)
    return s

def random_square_matrix(N):
    A = []
    for _ in range(N):
        A.append([randint(0, 100) for _ in range(N)])
    return A


tests = TestSet()

#
# ручные тесты
#
tests.add(
    question([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]),
    answer([
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ])
)
tests.add(
    question([
        ['1', '2', '3', '4'],
        ['5', '6', '7', '8'],
        ['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h']
    ]),
    answer([
        ['1', '5', 'a', 'e'],
        ['2', '6', 'b', 'f'],
        ['3', '7', 'c', 'g'],
        ['4', '8', 'd', 'h']
    ])
)
tests.add(
    question([
        [1]
    ]),
    answer([
        [1]
    ])
)
tests.add(
    question([
        ['abc', 'cde'],
        ['fgh', 'abc']]
    ),
    answer([
        ['abc', 'fgh'],
        ['cde', 'abc']
    ])
)
tests.add(
    question([
        [5]
    ]),
    answer([
        [5]
    ])
)

#
# автоматические тесты
#
for N in (10, 10, 10):
    A = random_square_matrix(N)
    q = question(A)
    transpose(A)
    a = answer(A)
    tests.add(q, a)

