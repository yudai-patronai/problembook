from lib.testgen import TestSet
from lib.random import randint


def lstrip_all(text):
    left_stripped_lines = [line.lstrip() for line in text.split('\n')]
    return '\n'.join(left_stripped_lines)


tests = TestSet()

tests.add(lstrip_all("""6
                     Party one
                     Party two
                     Party three
                     Party three
                     Party two
                     Party three"""),
          lstrip_all("""Party three
                     Party two
                     Party one"""))

tests.add(lstrip_all("""3
                     Ядро
                     КПРС
                     Ядро
                     Груша
                     КПРС
                     Ядро"""),
          lstrip_all("""Ядро
                     КПРС
                     Груша"""))

tests.add(lstrip_all("""5
                     Сноуден
                     Сноуден
                     Сноуден
                     Сноуден
                     Сноуден"""),
          "Сноуден")

tests.add("100\n" + "A\n"*49 + "B\n"*51, "B\nA\n")
