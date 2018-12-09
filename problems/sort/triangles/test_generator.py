#!/usr/bin/env python3
import os
import math
import shutil
import random

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

tests = [
    [('id1', 2, 3, 4), ('id2', 7, 8, 9), ('id3', 4, 5, 6)],
    [('triangle0', 2, 4, 3), ('triangle1', 1, 1, 1)]
]

def get_square(tr):
    a, b, c = tr[1], tr[2], tr[3]
    p = (a + b + c) / 2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def get_triangle_repr(tr):
    return '{} {} {} {}'.format(*tr)

def generate_triangle(i):
    id_ = 'id_' + str(i)
    a = random.randint(3, 300)
    b = random.randint(3, 300)
    c = random.randint(max(a, b), a+b-1)
    return (id_, a, b, c)

def generate_triangles(count):
    return [generate_triangle(i) for i in range(count)]

def write_test(tests_dir, ind, triangles):
    sorted_triangles = sorted(triangles, key=lambda tr: get_square(tr))
    N = len(sorted_triangles)

    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(str(N) + '\n')
        f.write('\n'.join(map(get_triangle_repr, triangles)))

    with open(ans, 'w') as f:
        f.write('\n'.join(map(get_triangle_repr, sorted_triangles)))


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i in range(3):
        tests.append(generate_triangles((i+10)*2))

    for i, data in enumerate(tests):
        write_test(tests_dir, i + 1, data)


write_tests(tests_dir)
