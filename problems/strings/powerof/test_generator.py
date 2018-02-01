import os
import shutil
from lib import random
import string

def solution(string, exponent):
    if exponent > 0:
        return string * exponent

    exponent = -exponent
    if len(string) % exponent != 0:
        return 'NO SOLUTION'
        
    base = string[:len(string) // exponent]
    return base if base * exponent == string else 'NO SOLUTION'

def str_generator(size=6, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

N = 10
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = 'abc'
        exponent = 3

    elif num == 2:
        seq = ' abcdabcd'
        exponent = -2

    elif num == 3:
        seq = 'abcd'
        exponent = -4

    elif num == 4:
        seq = str_generator(50)
        exponent = -1

    else:
        if num % 3 == 0:
            seq = str_generator(50)
            exponent = random.randint(-10, -2)
        elif num % 3 == 1:
            exponent = random.randint(2, 10)
            seq = str_generator(50) * exponent
        elif num % 3 == 2:
            exponent = random.randint(-10, -2)
            seq = str_generator(50) * -exponent

    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write('\n'.join([seq, str(exponent)]))

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(solution(seq, exponent))
