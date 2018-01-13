from lib.testgen import TestSet
from lib.random import randint

MAX_RAND_TESTS = 20

def get_rand_matrix(dim):
   matrix = [[randint(-20, 20) for _ in range(dim)] for _ in range(dim)]
   return matrix

def matrix_to_str(matrix):
    return '\n'.join(' '.join(map(str,row)) for row in matrix)

def get_case(dim, swap, matrix):
    maxval = matrix[0][0]
    maxrow = 0
    for i, row in enumerate(matrix):
        if row[i] > maxval:
            maxrow = i
            maxval = row[i]

    q_str = '{0} {1}\n'.format(dim, swap) + matrix_to_str(matrix)

    matrix[swap], matrix[maxrow] = matrix[maxrow], matrix[swap]
    ans_str = matrix_to_str(matrix)

    return q_str, ans_str

def get_random_case(dim):
    swap = randint(0, dim - 1)
    matrix = get_rand_matrix(dim)
    return get_case(dim, swap, matrix)

tests = TestSet()

tests.add(*get_case(3, 1,
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]))
tests.add(*get_case(4, 3,
    [[1, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 1]]))

for _ in range(MAX_RAND_TESTS):
    tests.add(*get_random_case(randint(1, 20)))
