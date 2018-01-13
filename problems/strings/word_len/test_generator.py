import os
import shutil
from lib import random
import string

def solution(string):
    Max = 0
    Min = 1001

    sorted_str = sorted(string.strip().split(' '), key=lambda x: len(x))
    print(sorted_str)
    return len(sorted_str[0]), len(sorted_str[-1])

def str_generator(size=6, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

N = 8
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = 'AAAA bbb aa'

    elif num == 2:
        seq = 'aaa ccc bbb'
    
    elif num == 3:
        seq = 'aaaa'

    elif num == 4:
        n_word = random.randint(5, 10)
        seq = ' '.join(list(map(str_generator, [random.randint(1, 1000) for i in range(n_word)])))
    
    else:
        n_word = random.randint(80, 150)
        seq = ' '.join(list(map(str_generator, [random.randint(5, 1000) for i in range(n_word)])))

    
    
    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(seq)

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(' '.join(map(str, solution(seq))))