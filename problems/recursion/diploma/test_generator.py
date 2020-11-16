from lib.testgen import TestSet
import lib.random as rand


base = 10
digits = range(base)
def gen_num(digit_count):
    num = 0
    for _ in range(digit_count):
        num = base * num + rand.choice(digits)
    return num


def bin_search(n, x, greater_or_equal):
    l, r = 0, n-1
    while l < r:
        m = (l + r) // 2
        if greater_or_equal(m, x):
            l, r = l, m
        else:
            l, r = m+1, r
    return l

def is_correct_square_side(side, whn):
    return (side // whn[0]) * (side // whn[1]) >= whn[2]

# Без учёта нулей, специально чтоб было различие с основной программой.
def calc_min_square_side(w, h, n):
    max_side = max(w, h) * n
    return bin_search(max_side + 1, (w, h, n), is_correct_square_side)


tests = TestSet()

tests.add('2 3 10\n', '9\n')
tests.add('1 1 1\n', '1\n')

USUAL_TESTS_COUNT = 2
for _ in range(USUAL_TESTS_COUNT):
    w, h, n = (gen_num(rand.randint(10, 60)) for _ in range(3))
    square_side = calc_min_square_side(w, h, n)
    # Если бинарный поиск возвращает отрицательное число, то это ошибка, поэтому выводим то, что точно не выведет основное решение
    tests.add('{} {} {}\n'.format(w, h, n), '{}\n'.format(square_side if square_side >= 0 else 'none'))

tests.add('0 0 0\n', '0\n')
tests.add('0 {} 0\n'.format(gen_num(98)), '0\n')

w = gen_num(60); n = gen_num(89)
tests.add('{} 0 {}\n'.format(w, n), '{}\n'.format(w))
tests.add('0 {} {}\n'.format(w, n), '{}\n'.format(w))

tests.add('{} {} 0\n'.format(gen_num(18), gen_num(45)), '0\n')
