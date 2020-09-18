import random
from lib.testgen import TestSet

random.seed(100)

def solution(n:int):
    return ((n % 4 == 0) and (n % 100 != 0)) or (n % 400 == 0)

def question(n:int):
    return str(n) + '\n'

def answer(b:bool):
    return 'YES\n' if b else 'NO\n'

tests = TestSet()
for n in 1, 2000, 400, 4, 100, 500, 1260, 1200, 791, 800:
    tests.add(question(n), answer(solution(n)))
