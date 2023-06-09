from lib.testgen import TestSet

MSG_INCORRECT = 'incorrect'

manual_tests = [
    (  # повторное использование переменной
        [ # (x-1)^3 = x^3 - 3x^2 + 3x - 1
            'x x x * * 3 x x * * - 3 x * + 1 - =',
            'x 3 ='
        ],
        '8'
    ),
    (  # не хватает операндов (см. первый минус)
        [
            '2 - x * 10 y 2 + * - =',
            'x 1 =',
            'y 1 ='
        ], 
        MSG_INCORRECT
    ),
    (  # не сообщена переменная x_1
        [
            'x_1 x_2 + 10 * =',
            'x_2 1 =',
            'y_1 2 =',
        ],
        MSG_INCORRECT
    ),
    (  # переменные с длинными именами
        [ # 10 * (x1^2 + x_2)
            'x_1 x_1 * x_2 + 10 * =',
            'x_1 -2 =',
            'x_2 1 ='
        ],
        '50'
    ),
    (  # три переменные
        [ # (aaa + bbb + ccc) // 3
            'aaa bbb + ccc + 3 / =',
            'aaa 2 =',
            'ccc 1 =',
            'bbb 1 ='
        ],
        '1' # 4 // 3 = 1
    ),
    (  # некорретное имя переменной в выражении
        [
            '0x y + =',
            'x 1 =',
            'y 1 =',
        ],
        MSG_INCORRECT
    ),
    (  # некорректное имя переменной в блоке инициализации
        [
            'x y + =',
            '0x 1 =',
            'y 1 =',
        ],
        MSG_INCORRECT
    ),
    (  # не сообщена переменная (скрытый тест)
        [
            'x y + =',
            'z 1 =',
            'x 1 ='
        ],
        MSG_INCORRECT
    ),
    (  # нет баланса между операторами и операндами
        [
            '2 2 - + =',
        ],
        MSG_INCORRECT
    ),
    (  # сложное выражение со всеми операндами
        [  # (a-x)^2 + b^2*(y-x^2) // b   # rosenbrock
            'a x - a x - * b b * y x x * - * b / + =',
            'a 1 =',
            'b 100 =',
            'x 2 = ',
            'y 3 =',
        ],
        '-99'
    ),
    (  # сложное выражение со всеми операндами без переменных
        [  # (a-x)^2 + b^2*(y-x^2) // b   # rosenbrock
            '1 2 - 1 2 - * 100 100 * 3 2 2 * - * 100 / + =',
        ],
        '-99'
    )
]

tests = TestSet()

for program, ans in manual_tests:
    tests.add(
        '\n'.join(program) + '\n',
        ans + '\n'
    )
