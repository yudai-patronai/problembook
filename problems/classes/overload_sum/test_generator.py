from lib.testgen import TestSet
from lib.random import randint
from lib import random
import string

MAX_RAND_LEN = 20
MAX_RAND_TESTS = 20
LENGTH_OF_WORDS = 30
ALPHABET = list(string.ascii_lowercase)

def generate_random_string():
    s = []
    alphabet = random.sample(ALPHABET, 20)
    for i in range(LENGTH_OF_WORDS):
        s.append(random.choice(alphabet))

    return "".join(s)

def generate_sequence(n):
    seq = []
    for i in range(n):
        number = randint(1, 1000)
        couple = (number, generate_random_string())
        seq.append(couple)
    return seq

def get_case(seq, seq2):
    question = '{}\n'.format(len(seq))
    for a in seq:
        question += ' '.join(str(k) for k in a)
        question += '\n'
    question += '{}\n'.format(len(seq2))
    for a in seq2:
        question += ' '.join(str(k) for k in a)
        question += '\n'
    question = question[:-1]
    ans = set(set(seq) | set(seq2))
    answer = ""
    for a in seq:
        for b in ans:
            if (a == b):
                answer += ' '.join([str(x) for x in a])
                answer += '\n'
    for a in seq2:
        for b in ans:
            if (a == b):
                answer += ' '.join([str(x) for x in a])
                answer += '\n'
    answer = answer[:-1]
    return question, answer

tests = TestSet()

for _ in range(MAX_RAND_LEN):
    tests.add(*get_case(generate_sequence(randint(1,MAX_RAND_LEN)),generate_sequence(randint(1,MAX_RAND_LEN))))
