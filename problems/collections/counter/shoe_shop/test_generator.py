#!/usr/bin/env python3
import os
import shutil

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')


tests = [
    [(2, 3, 4, 5, 6, 8, 7, 6, 5, 18), [(6, 55), (6, 45), (6, 55), (4, 40), (18, 60), (10, 50)], 200],
    [(2), [(1, 10)], 0],
    [(3, 3), [(1, 10), (3, 3), (3, 1), (3, 10)], 4],
    [(1, 2, 3), [(2, 1)], 1],
    [(1, 7, 7, 1), [(7, 1), (7, 1), (1, 3)], 5],
]


def write_test(tests_dir, ind, data):
    sizes, customers, answ = data
    X, N = len(sizes), len(customers)

    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write(str(X) + '\n')
        f.write(' '.join(map(str, sizes)) + '\n')
        f.write(str(N) + '\n')
        f.write('\n'.join(['{} {}'.format(s, m) for s, m in customers]))

    with open(ans, 'w') as f:
        f.write(str(answ) + '\n')


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i, data in enumerate(tests):
        write_test(tests_dir, i + 1, data)


write_tests(tests_dir)
