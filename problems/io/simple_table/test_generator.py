from lib.testgen import TestSet
from lib.random import choice, seed

seed(10)

NUMBER_OF_TESTS = 10
CHARS = '0123456789abcdefghijklmnopqrstuvwxyz'

def question_data():
    return  tuple( choice(CHARS) for _ in range(3) ), tuple( choice(CHARS) for _ in range(3) ) 

def question(qdata):
    return '{} {} {}\n{} {} {}\n'.format(*qdata[0], *qdata[1])

def answer(qdata):
    return '{} | {} | {}\n---------\n{} | {} | {}\n'.format(*qdata[0], *qdata[1])

tests = TestSet()

for _ in range(NUMBER_OF_TESTS):
    qdata = question_data()
    tests.add(question(qdata), answer(qdata))