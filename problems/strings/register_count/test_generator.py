import os
import shutil
from lib import random
import string

def solution(string):
    upper = 0
    lower = 0

    for symbol in string:
        if ord(symbol) >= ord('a') and ord(symbol) <= ord('z'):
            lower += 1
        elif ord(symbol) >= ord('A') and ord(symbol) <= ord('Z'):
            upper += 1

    return upper, lower

def str_generator(size=6, chars=string.ascii_letters + string.digits + ' ' + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


N = 8
random.seed(1984)

tests_dir = os.path.join(os.path.dirname(__file__), 'tests')

shutil.rmtree(tests_dir, ignore_errors=True)
os.makedirs(tests_dir)

for num in range(1, N + 1):
    if num == 1:
        seq = 'AAAaa BBb'

    elif num == 2:
        seq = 'AA0009999  00'
    
    elif num == 3:
        seq = 'aa___=++dsd00 ;;;$$$$$@@@'

    elif num == 4:
        seq = str_generator(20)
    
    else:
        seq = str_generator(1000)

    
    
    with open(os.path.join(tests_dir, '{0:0>2}'.format(num)), 'w') as f:
        f.write(seq)

    with open(os.path.join(tests_dir, '{0:0>2}.a'.format(num)), 'w') as f:
        f.write(' '.join(map(str, solution(seq))))