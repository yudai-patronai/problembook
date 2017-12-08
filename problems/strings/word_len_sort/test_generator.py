import os
import shutil
from lib import random
import string

def solution(string):
    raw_sorted = sorted(string.split(' '), key=lambda x: len(x))
    return [sum([ord(i) for i in word]) for word in raw_sorted]

def str_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

N = 8
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = 'abcd hi efg'

    elif num == 2:
        seq = 'XX YyY' 
    
    elif num == 3:
        seq = 'ZzZ'

    elif num == 4:
        word_len = random.sample(range(5, 15), 5)
        seq = ' '.join(list(map(str_generator, word_len)))
    
    else:
        word_len = random.sample(range(5, 150), 50)
        seq = ' '.join(list(map(str_generator, word_len)))
    
    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(seq)

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(' '.join(map(str, solution(seq))))
