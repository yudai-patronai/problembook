#!/usr/bin/env python3

import os
from lib import random
#import random
import shutil

random.seed('friends')

def random_q():
    n = random.randint(5, 100)
    s = random.randint(0, n-1)
    a = list()
    for i in range(n):
        row = [round(random.randint(62) / 100 ) for _ in range(n)]
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


tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for test in range(4, 21):
    N, S, A = random_q()
    firstst = str(N)+' '+str(S)
    matstring = ""
    for el in A:
        matstring += '\n' + ' '.join(map(str, el))
    ans = solve(N, S, A)
    with open(os.path.join(tests_dir, '{0:0>2}'.format(test)), 'w') as f:
        f.write(firstst + matstring)
    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(test)), 'w') as f:
        f.write(str(ans))
with open(os.path.join(tests_dir, '01'), 'w') as f:
    f.write('3 1\n')
    f.write('0 1 1\n0 0 1\n0 0 0')
with open(os.path.join(tests_dir, '01.a'), 'w') as f:
    f.write('2')
with open(os.path.join(tests_dir, '02'), 'w') as f:
    f.write('2 1\n')
    f.write('0 1\n0 0')
with open(os.path.join(tests_dir, '02.a'), 'w') as f:
    f.write('1')
with open(os.path.join(tests_dir, '03'), 'w') as f:
    f.write('4 1\n')
    f.write('0 0 0 0\n0 0 1 1\n0 0 0 1\n0 0 0 0')
with open(os.path.join(tests_dir, '03.a'), 'w') as f:
    f.write('2')
