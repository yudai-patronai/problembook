import os
import shutil
from lib import random
import string

def solution(s):
    l = len(s)
    abs_max = 0
    cur_max = 1
    i = 0
    while i < l-1:
        if (s[i] == s[i+1]) :
            cur_max += 1
        else:
            abs_max = max(abs_max, cur_max)
            cur_max = 1
        i += 1
    abs_max = max(abs_max, cur_max)
    return abs_max

def str_generator(size=6, chars=string.ascii_letters+string.digits+' '):
    return ''.join(random.choice(chars) for _ in range(size))

N = 10
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = 'mipt'
    elif num == 2:
        seq = 'WazzzZZzup'
    elif num == 3:
        seq = 'p'
    elif num == 4:
        seq = 'maxmaxmax 444'
    elif num == 5:
        seq = str_generator(512)
    else:
        seq = str_generator(50)
        
    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(seq + '\n')

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(str(solution(seq)))