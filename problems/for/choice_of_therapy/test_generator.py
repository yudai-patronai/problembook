# test_generator.py
from lib.testgen import TestSet

tests = TestSet()
# Some basic tests
tests.add('6 3 8 6 4 7 5\n', '13\n')
tests.add('10 1 14 23 54 98 12 92 99 2 10\n', '197\n')
tests.add('4 10 2 22 4\n', '0\n')
tests.add('3 21 3 5\n', '0\n')
tests.add('11 12 32 34 54 11 2 3 45 55 6 90\n', '109\n')
tests.add('5 12 11 13 23 43\n', '23\n')
tests.add('7 120 98 87 299 350 401 543\n', '751\n')
tests.add('8 998 1002 1230 90 99 490 380 343\n', '1097\n')
