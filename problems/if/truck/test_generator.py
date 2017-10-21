#!/usr/bin/env python3
import os
import shutil

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

tests = (
#     t_w t_h p_w p_h f_w f_h m_w m_h    ans
    ((( 1,  1,  5, 10,  5, 10, 10, 10),  'NO'),
     (( 1,  1,  5, 10,  5, 10, 11, 11), 'YES'),
     (( 1,  1,  5, 10,  5, 10, 10, 11), 'YES'),
     (( 1,  1,  5, 10,  5, 10,  5, 11),  'NO'),
     (( 1,  1,  5, 10,  5, 10, 11, 10),  'NO'),
     (( 1,  1,  5, 10,  5,  7, 11, 10), 'YES'),
     (( 1,  1,  5,  5,  5, 10, 11, 10),  'NO'),
     (( 1,  1,  6, 10,  5,  7, 11, 10),  'NO'),
     (( 1,  1, 11, 10,  5,  7, 11, 11),  'NO'))
)


def write_test(tests_dir, ind, data):
    test = os.path.join(tests_dir, '%.2d' % ind)
    ans = test + '.a'

    with open(test, 'w') as f:
        f.write('\n'.join(map(str, data[0])) + '\n')

    with open(ans, 'w') as f:
        f.write(data[1] + '\n')


def write_tests(tests_dir):
    shutil.rmtree(tests_dir, ignore_errors=True)
    os.makedirs(tests_dir)

    for i, t in enumerate(tests):
        write_test(tests_dir, i, t)


write_tests(tests_dir)
