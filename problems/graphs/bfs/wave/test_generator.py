#!/usr/bin/env python3
import os
import shutil

import solution

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

# a - start
# b - end
# B - end on X
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
"""

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
