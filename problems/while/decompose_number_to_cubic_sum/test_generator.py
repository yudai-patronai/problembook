#!/usr/bin/python3

import os
import shutil

test_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

# пары должны быть упорядочены по неубыванию
questions = [      8,    432,          314,    3591,         8274,    5832,    96957,    43904, 1028196  ]
answers   = [ (0, 2), (6, 6), 'impossible', (6, 15), 'impossible', (0, 18), (18, 45), (28, 28), (65, 91) ]


for test_num, qa in enumerate( zip(questions, answers) ):
    test_num += 1
    
    q, a = qa

    with open(os.path.join(test_dir, '{0:0>2}'.format(test_num)), 'w') as f:
        f.write("{}\n".format(q))
    
    with open(os.path.join(test_dir, '{0:0>2}.a'.format(test_num)), 'w') as f:
        if a == 'impossible':
            f.write("{}\n".format(a))
        else:
            f.write("{} {}\n".format(*a))