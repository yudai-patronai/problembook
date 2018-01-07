#!/usr/bin/env python3
import os
import shutil

tests = [
'''
00000000
00000000
00000000
00000000
00w00000
00000000
00000000
00000000
''',
'''
000b0000
00bb0000
000b0000
0000w000
00000000
00000000
00000000
00000000
''',
'''
00000000
00000000
0000w000
00000000
00000000
00000000
00000000
00000000
''',
'''
0000b000
0000b000
0000w000
00000000
00000000
00000000
00000000
00000000
''',
'''
bbbbbbbb
bbbbbbbb
bbbbbbbb
000w0000
00000000
00000000
00000000
00000000
''',
'''
bbbbbbbb
bbbbbbbb
bbwbbbbb
00000000
00000000
00000000
00000000
00000000
''',
'''
bbbbbbbb
bbbbbbbb
bbbbbbbb
bbbbbbbb
bbbbbbbb
bbbbbbbb
bwbbbbbb
bbbbbbbb
''',
'''
000bbb00
0000b00b
00000b0b
000000b0
0000000w
00000000
00000000
00000000
''',
'''
bbbwbbbb
00000000
00000000
00000000
00000000
00000000
00000000
00000000
''',
'''
00000000
0b00bb00
00b0b000
000b0b00
0000b000
00000b00
000000b0
0000000w
'''
]


def write_test(fname, test):
    black = []
    for i, s in enumerate(test.split('\n')):
        for j, c in enumerate(s):
            if c == 'w':
                white = chr(j + ord('a')) + str(9 - i)
            elif c == 'b':
                black.append(chr(j + ord('a')) + str(9 - i))

    with open(fname, 'w') as f:
        f.write(str(len(black)) + '\n')
        if black:
            f.write('\n'.join(black) + '\n')
        f.write(white + '\n')

    os.system('python3 solution.py < ' + fname + ' > ' + fname + '.a')


def write_tests(tests_dir, tests):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i, t in enumerate(tests):
        write_test(os.path.join(tests_dir, '%.2d' % (i + 1)), t)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
write_tests(tests_dir, tests)
