#!/usr/bin/env python3

from lib import random
from lib.testgen import TestSet

random.seed('friends')


def array2d_to_str(A):
    s = ''
    for row in A:
        s += ' '.join(map(str, row)) + '\n'
    return s

def str_question(A:list, S:int):  # A - матрица дружбы, S - человек из условия
    q = '{} {}\n{}'.format(len(A), S, array2d_to_str(A))
    if not q.endswith('\n'):
        q += '\n'
    return q

def str_answer(ans:int):
    return str(ans) + '\n'

def random_q():
    n = random.randint(5, 100)
    s = random.randint(0, n-1)
    a = list()
    for i in range(n):
        row = [round(random.randint(59) / 100 ) for _ in range(n)]
        a.append(row)
    for i in range(n):
        a[i][i] = 0
    return n, s, a

def dfs(start, graph, visited):
    visited[start] = True
    for i in range(len(graph)):
        if (graph[start][i] == 1 or graph[i][start] == 1) and not visited[i]:
            dfs(i, graph, visited)

def solve(n, s, a):
    used = [False] * n
    dfs(s, a, used)
    return (sum(used) - 1)


Tests = TestSet()

manual_tests = [
    ([  # матрица дружбы, номер человека, ответ
        [0, 1, 1],
        [0, 0, 1],
        [0, 0, 0],
    ], 1, 2),  
    ([
        [0, 1],
        [0, 0],
    ], 1, 1),
    ([
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ], 1, 2),
]

for A, S, ans in manual_tests:
    Tests.add(str_question(A, S), str_answer(ans))

for _ in range(4, 21):
    N, S, A = random_q()
    ans = solve(N, S, A)
    Tests.add(str_question(A, S), str_answer(ans))
