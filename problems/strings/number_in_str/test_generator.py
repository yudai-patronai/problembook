import os
import shutil
from lib import random
import string
import re
from functools import reduce
import operator

def solution(strs):
    splited = [int(i) for i in re.split(r'[^0-9]', strs) if i != '']
    return reduce(operator.mul, splited, 1)

def str_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

N = 8
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = 'kjjjkkj2.5jkjn,,,hfd45jgfvjlkfdii10,2hfhg'

    elif num == 2:
        seq = 'aaa23b3n3' 
    
    elif num == 3:
        seq = '2a44'

    elif num == 4:
        numbers_len = [random.randint(1, 5) for i in range(5)]
        numbers = [str_generator(i, string.digits) for i in numbers_len]

        word_len = [random.randint(1, 50) for i in range(5)]
        word = [str_generator(i, string.ascii_letters + string.punctuation) for i in numbers_len]

        result = [None]*(len(numbers)+len(word))
        result[::2] = word
        result[1::2] = numbers
        seq = ''.join(result)
    
    else:
        word_len = random.sample(range(5, 150), 50)
        seq = ' '.join(list(map(str_generator, word_len)))
    
    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(seq)

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(str(solution(seq)))
