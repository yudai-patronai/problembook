from lib.testgen import TestSet


def question(N, K, coords):
    return '{} {}\n'.format(N, K) + ' '.join(map(str, coords)) + '\n'

def answer(d):
    return str(d) + '\n'


qa = [
    (6, 3, [2, 5, 7, 11, 15, 20], 9),
    (7, 3, [1, 2, 3, 4, 5, 6, 7], 3),
    (4, 3, [1, 2, 3, 10], 2),
    (4, 3, [1, 4, 7, 15], 6),
    (10001, 3, list(range(10001)), 5000) # линейный поиск должен не пройти
]


tests = TestSet()

for N, K, coords, d in qa:
    tests.add(question(N, K, coords), answer(d))
