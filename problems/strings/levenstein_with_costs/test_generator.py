from lib.testgen import TestSet


def question(insert, remove, replace, a, b):
    return '{} {} {}\n{}\n{}\n'.format(insert, remove, replace, a, b)


def answer(cost):
    return '{}\n'.format(cost)


qa = [
    ( 
        (1, 1, 1, 'aaa', 'bbb'),
        3,
    ),
    ( 
        (1, 1, 3, 'aaa', 'bbb'),
        6,
    ),
    ( 
        (1, 2, 1, 'aaababb', 'bbb'),
        8,
    ),
    ( 
        (1, 1, 1, 'kolokol',
                  'moloko'),
        2,
    ),
    ( 
        (1, 2, 1, 'kolokol',
                  'moloko'),
        3,
    ),
    ( 
        (1, 2, 4, 'kolokol',
                  'moloko'),
        5,
    ),
]

tests = TestSet()

for q, a in qa:
    tests.add(question(*q), answer(a))
