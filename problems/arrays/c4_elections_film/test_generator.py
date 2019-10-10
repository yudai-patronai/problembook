from lib.testgen import TestSet
from lib.random import randint

RAND_TESTS_NUM = 0
MAX_RAND_NUM = 10 ** 3

def get_case(num):
    films_number = randint(1, num)
    ans = 'YES' if num & (num - 1) == 0 else 'NO'
    return str(num), ans


def lstrip_all(text):
    left_stripped_lines = [line.lstrip() for line in text.split('\n')]
    return '\n'.join(left_stripped_lines)


tests = TestSet()

tests.add(lstrip_all("""6
                     Белое солнце пустыни
                     Бриллиантовая рука
                     Белое солнце пустыни
                     Белое солнце пустыни
                     Гараж
                     Бриллиантовая рука"""),
          lstrip_all("""Белое солнце пустыни 3
                     Бриллиантовая рука 2
                     Гараж 1"""))

tests.add(lstrip_all("""3
                     Разум и чувства
                     Гордость и предубеждение
                     Гордость и предубеждение"""),
          lstrip_all("""Гордость и предубеждение 2
                     Разум и чувства 1"""))

tests.add(lstrip_all("""5
                     Сноуден
                     Сноуден
                     Сноуден
                     Сноуден
                     Сноуден"""),
          "Сноуден 5")

for _ in range(RAND_TESTS_NUM):
	tests.add(*get_case(randint(MAX_RAND_NUM)))
