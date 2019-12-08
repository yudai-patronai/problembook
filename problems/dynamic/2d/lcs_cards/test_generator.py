from lib.testgen import TestSet

def question(a, b):
    return ' '.join(map(str, a)) + '\n' + ' '.join(map(str, b)) + '\n'

def answer(yesno):
    return yesno + '\n'


qa = [
    (
        (1, 2, 3, 4, 5, 6, 7, 8),
        (1, 2, 3, 8, 7, 6, 5, 4),
        'NO'
    ),
    (
        (1, 5, 2, 8, 6, 4, 7, 3),
        (3, 7, 4, 2, 6, 5, 1, 8),
        'YES'
    ),
    (
        (1, 2, 3, 4, 5, 6, 7, 8),
        (8, 7, 6, 5, 4, 3, 2, 1),
        'YES'
    ),
    (
        (1, 5, 2, 8, 6, 4, 7, 3),
        (6, 7, 3, 2, 4, 5, 1, 8),
        'NO'
    ),
]

tests = TestSet()

for a, b, ans in qa:
    tests.add(question(a, b), answer(ans))
