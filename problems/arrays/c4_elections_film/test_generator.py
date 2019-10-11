from lib.testgen import TestSet
from lib.random import randint


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

tests.add("100\n" + "A\n"*49 + "B\n"*51, "B 51\nA 49\n")
