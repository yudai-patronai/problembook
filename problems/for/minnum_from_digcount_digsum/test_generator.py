#!/usr/bin/python3

import os
import shutil

test_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(test_dir, ignore_errors=True)
os.makedirs(test_dir)

questions = [ (4, 2),       (4, 5),      (25, 2), (35, 6),   (58, 8),      (62, 4), (34, 7), ]
answers   = [     13, 'impossible', 'impossible',  116999,  13999999, 'impossible', 1114999, ]

for test_num, qa in enumerate( zip(questions, answers) ):
    test_num += 1
    
    q, a = qa

    with open(os.path.join(test_dir, '{0:0>2}'.format(test_num)), 'w') as f:
        f.write("{} {}\n".format(*q))
    
    with open(os.path.join(test_dir, '{0:0>2}.a'.format(test_num)), 'w') as f:
        f.write("{}\n".format(a))
