from lib.testgen import TestSet
from lib.random import randint


def lstrip_all(text):
    left_stripped_lines = [line.lstrip() for line in text.split('\n')]
    return '\n'.join(left_stripped_lines)


tests = TestSet()

tests.add(lstrip_all("""6
                     Beloe solnce pustyni
                     Brilliantovaya ruka
                     Beloe solnce pustyni
                     Beloe solnce pustyni
                     Garazh
                     Brilliantovaya ruka"""),
          lstrip_all("""Beloe solnce pustyni 3
                     Brilliantovaya ruka 2
                     Garazh 1"""))

tests.add(lstrip_all("""3
                     Razum i chuvstva
                     Gordost' i predubezhdenie
                     Gordost' i predubezhdenie"""),
          lstrip_all("""Gordost' i predubezhdenie 2
                     Razum i chuvstva 1"""))

tests.add(lstrip_all("""5
                     Snouden
                     Snouden
                     Snouden
                     Snouden
                     Snouden"""),
          "Snouden 5")

tests.add("100\n" + "A\n"*49 + "B\n"*51, "B 51\nA 49\n")
