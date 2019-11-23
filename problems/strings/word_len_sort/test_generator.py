from lib.testgen import TestSet
from lib import random
import string

def solution(string):
    raw_sorted = sorted(string.split(' '))
    raw_sorted = sorted(raw_sorted, key=lambda x: len(x))
    return [sum([ord(i) for i in word]) for word in raw_sorted]

def str_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

N = 9
random.seed(1984)
tests = TestSet()

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
    elif num == 5:
        seq = 'bb bbb aaa'
    else:
        word_len = random.sample(range(5, 150), 50)
        seq = ' '.join(list(map(str_generator, word_len)))
    
    tests.add(seq + '\n', ' '.join(map(str, solution(seq))) + '\n')
