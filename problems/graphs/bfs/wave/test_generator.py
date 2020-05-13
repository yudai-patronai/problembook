#!/usr/bin/env python3
from lib import random
from lib.testgen import TestSet

random.seed(100)

INF_VAL = 'INF'

Tests = TestSet()

#####
##### Ручные тесты
#####

manual_tests = [
{
    'field':
"""XXXXXXX
X X   X
X X X X
X   X X
XXXXXXX
""", 'start': (3, 5), 'end': (1, 1), 'ans': 10
},
{
    'field':
"""XXXXXXX
X X   X
X XXX X
X   X X
XXXXXXX
""", 'start': (3, 5), 'end': (1, 1), 'ans': INF_VAL
},
{
    'field':
"""XXXXXXX
X     X
X X X X
X   X X
XXXXXXX
""", 'start': (3, 5), 'end': (1, 1), 'ans': 6
},
{
    'field':
"""XXXXXXX
X     X
XXX X X
X     X
XXXXXXX
""", 'start': (3, 5), 'end': (1, 1), 'ans': 6
},
{  # конечная точка - стена
    'field':
"""XXXXXXX
XX    X
X     X
X     X
XXXXXXX
""", 'start': (3, 5), 'end': (1, 1), 'ans': INF_VAL
},
{
    'field':
"""XXXXXXX
X X   X
XXX X X
    X X
XXXXXXX
""", 'start': (3, 5), 'end': (1, 1), 'ans': INF_VAL
},
{
    'field':
"""XXXXXXX
X     X
X c   X
X     X
XXXXXXX
""", 'start': (2, 2), 'end': (2, 2), 'ans': 0
}
]

for t in manual_tests:
    field_str = t['field']

    question = '{N} {M}\n{start_n} {start_m}\n{end_n} {end_m}\n{field}'.format(
        N=field_str.count('\n'),
        M=field_str.find('\n'),
        start_n=t['start'][0],
        start_m=t['start'][1],
        end_n=t['end'][0],
        end_m=t['end'][1],
        field=field_str
    )

    if not question.endswith('\n'):  # для удобства, если в лабиринте забыли '\n' в конце
        question += '\n'

    ans = str(t['ans']) + '\n'
    Tests.add(question, ans)

#####
##### Случайные тесты: убраны, см. предыдущие коммиты по этой задаче, где был написан генератор
#####

# большое поле без стенок - можно асимптотику проверять
N, M = 50, 50
start = 0, 0
end = N-1, M-1

field = (' ' * M + '\n') * N
ans = abs(start[0] - end[0]) + abs(start[1] - end[1])

Tests.add(
    '{} {}\n{} {}\n{} {}\n{}'.format(N, M, *start, *end, field),
    str(ans) + '\n'
)
