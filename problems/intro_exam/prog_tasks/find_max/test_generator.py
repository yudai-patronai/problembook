from lib.testgen import TestSet
from lib.random import randint, seed

seed(181)

def gen_arr():
    size = randint(3, 50)

    return [ randint(-100, 100) for _ in range(size) ]

def question(arr):
    return '\n'.join(map(str, arr)) + '\n' + '#' + '\n'

def answer(num):
    return str(num) + '\n'

tests = TestSet()

tests.add('1\n2\n-1\n#\n', '2\n')

for _ in range(8):
    arr = gen_arr()
    ans = max(arr)

    tests.add(question(arr), answer(ans))

tests.add('1\n#\n', '1\n')
