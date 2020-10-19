from lib.testgen import TestSet
from lib.random import choice, random, randrange, seed

seed(42)


second_names = ["Pupkin", "Ivanov", "Petrov", "Solovyova", "Grigorieva", "Shabanov", "Erokhin", "Kraznopuzova"]

name = lambda: choice(second_names)
hour = lambda: round(randrange(10, 200) + randrange(0, 9) / 10, 1)
score = lambda: randrange(0, 10)


def question(sname, hour_scores):
    return sname + '\n' + ' '.join(map(str, hour_scores)) + '\n'

def answer(sname, hours, avg_score):
    return '{} {} {}\n'.format(sname, hours, avg_score)

def gen_question():
    return name(), [hour(), score(), hour(), score(), hour(), score()]

def gen_answer(name, hour_scores):
    hours_math, score_math, hours_physics, score_physics, hours_cs, score_cs = hour_scores
    sum_hours = hours_math + hours_physics + hours_cs
    sum_scores = score_math + score_physics + score_cs

    return name, round(sum_hours, 1), round(sum_scores/3, 1)

tests = TestSet()
tests.add(question('Pupkin', [75.5, 8, 105.5, 9, 45.1, 8]), answer('Pupkin', 226.1, 8.3))

for _ in range(9):
    n, hour_scores = gen_question()
    n, h, s = gen_answer(n, hour_scores)

    tests.add(question(n, hour_scores), answer(n, h, s))
