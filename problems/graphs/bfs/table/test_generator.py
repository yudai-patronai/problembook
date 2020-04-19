#!/usr/bin/env python3

from lib import random
from queue import Queue
from lib.testgen import TestSet

random.seed(265)
NUM_RANDOM_TESTS = 7

# доля единиц в таблице будет 1 / RARENESS_OF_ONES, остальное - единицы
RARENESS_OF_ONES = 10

def solver(n, m, a):
    q = Queue()
    d = [[-1] * m for _ in range(n)]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            if a[i][j]:
                d[i][j] = 0
                q.put((i, j))

    while not q.empty():
        x, y = q.get()
        for dx, dy in moves:
            if 0 <= x + dx < n and 0 <= y + dy < m and \
                    d[x + dx][y + dy] == -1:
                d[x + dx][y + dy] = d[x][y] + 1
                q.put((x + dx, y + dy))

    return d

def matrix_to_str(matrix:list):
    s = ''
    for row in matrix:
        s += ' '.join(map(str, row)) + '\n'
    return s


tests = TestSet()

# manual tests
tests.add(
"""5 5
0 0 1 0 0
0 1 0 0 0
0 0 0 1 0
0 0 0 0 0
1 0 0 0 1
""",
"""2 1 0 1 2
1 0 1 1 2
2 1 1 0 1
1 2 2 1 1
0 1 2 1 0
"""
)
tests.add(
"""4 4
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 1
""",
"""0 1 2 3
1 2 3 2
2 3 2 1
3 2 1 0
"""
)
tests.add('1 1\n1\n', '0\n')

# размер входных данных = 2 * (rows * cols + len(str(rows)) + len(str(cols)))
#   (с учётом пробелов и символов переноса, расстояния от 0 до 9)
#
# rows * cols <= 30000, иначе ежадж (апрель 2020) может упасть от размера входных данных
#   наибольший тест, проходивший на ежадж, имел размер 30952
#   68000 символов точно перебор, однако, тестов в интервале от 30000 до 68000 не было

for _ in range(NUM_RANDOM_TESTS):
    rows = random.randint(10, 300)
    cols = random.randint(10, 100)

    # количество единиц составляет 1 / RARENESS_OF_ONES от количества элементов в таблице
    table = [[ 1 if random.randint(1, RARENESS_OF_ONES) == 1 else 0 for _ in range(cols)] for _ in range(rows)]

    tests.add(
        '{} {}\n'.format(rows, cols) + matrix_to_str(table),
        matrix_to_str(solver(rows, cols, table))
    )
