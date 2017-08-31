#!/usr/bin/env python3
import os
import random
import shutil

import solution

random.seed(100)
tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

# a - start
# b - end
# B - end on X
# c - start and end in one empty cell
tests = """
XXXXXXX
XbX   X
X X X X
X   XaX
XXXXXXX

XXXXXXX
XbX   X
X XXX X
X   XaX
XXXXXXX

XXXXXXX
Xb    X
X X X X
X   XaX
XXXXXXX

XXXXXXX
Xb    X
XXX X X
X    aX
XXXXXXX

XXXXXXX
XB    X
X     X
X    aX
XXXXXXX

XXXXXXX
XbX   X
XXX X X
    XaX
XXXXXXX

XXXXXXX
X     X
X c   X
X     X
XXXXXXX
"""


def draw_hline(field, i, j1, j2):
    for j in range(j1, j2 + 1):
        field[i][j] = -2


def draw_vline(field, i1, i2, j):
    for i in range(i1, i2 + 1):
        field[i][j] = -2


def gen_field(n, m):
    field = [[-1] * m for _ in range(n)]

    ia = 0.7
    ib = 0.3
    ja = 0.7
    jb = 0.3

    for _ in range(round(n * ia)):
        c = random.randrange(1, round(n * ib))
        i = random.randrange(n)
        j = random.randrange(m - c)
        draw_hline(field, i, j, j + c)

    for _ in range(round(m * ja)):
        c = random.randrange(1, round(m * jb))
        i = random.randrange(n - c)
        j = random.randrange(m)
        draw_vline(field, i, i + c, j)

    return field


# Not sure that longest, but should be long enough =)
def find_longest_way(field):
    n = len(field)
    m = len(field[0])

    max_len = 0

    for i in range(n):
        for j in range(m):
            if field[i][j] == -1:
                i2, j2 = solution.wave(field, i, j)
                if field[i2][j2] > max_len:
                    max_way = (i, j, i2, j2)
                    max_len = field[i2][j2]

    return max_way


shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

tests = [t.split('\n') for t in tests.strip().split('\n\n')]
ind = 1
for t in tests:
    print(ind)
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == 'a':
                i1 = i
                j1 = j
                tt = list(t[i])
                tt[j] = ' '
                t[i] = ''.join(tt)
            elif t[i][j] == 'b':
                i2 = i
                j2 = j
                tt = list(t[i])
                tt[j] = ' '
                t[i] = ''.join(tt)
            elif t[i][j] == 'B':
                i2 = i
                j2 = j
                tt = list(t[i])
                tt[j] = 'X'
                t[i] = ''.join(tt)
            elif t[i][j] == 'c':
                i1 = i
                j1 = j
                i2 = i
                j2 = j
                tt = list(t[i])
                tt[j] = ' '
                t[i] = ''.join(tt)

    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'
    ind += 1

    with open(test, 'w') as f:
        f.write('%d %d\n' % (len(t), len(t[0])))
        f.write('%d %d\n' % (i1, j1))
        f.write('%d %d\n' % (i2, j2))
        f.write('\n'.join(t) + '\n')

    with open(ans, 'w') as f:
        f.write(solution.solve(i1, j1, i2, j2, solution.read_field_from_array(t)))

for i in range(1, 40):
    print(ind)

    n = random.randrange(i * 12, (i + 1) * 12)
    m = random.randrange(i * 12, (i + 1) * 12)
    field = gen_field(n, m)
    if i % 5 == 0:
        i1 = random.randrange(n)
        j1 = random.randrange(m)
        i2 = random.randrange(n)
        j2 = random.randrange(m)
    else:
        i1, j1, i2, j2 = find_longest_way(field)

    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'
    ind += 1

    with open(test, 'w') as f:
        f.write('%d %d\n' % (n, m))
        f.write('%d %d\n' % (i1, j1))
        f.write('%d %d\n' % (i2, j2))
        f.write('\n'.join([''.join(['X' if x == -2 else ' ' for x in row]) for row in field]) + '\n')

    with open(ans, 'w') as f:
        f.write(solution.solve(i1, j1, i2, j2, field))

# big empty field
print(ind)
test = os.path.join(tests_dir, '%.2d' % ind)
ans = test + '.a'
ind += 1
n = 500

with open(test, 'w') as f:
    f.write('%d %d\n' % (n, n))
    f.write('%d %d\n' % (0, 0))
    f.write('%d %d\n' % (n - 1, n - 1))
    row = ' ' * n + '\n'
    for _ in range(n):
        f.write(row)

with open(ans, 'w') as f:
    f.write('%d\n' % (n * 2 - 2))
