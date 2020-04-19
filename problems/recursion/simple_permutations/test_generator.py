# test_generator.py
from lib.testgen import TestSet

tests = TestSet()
# Some basic tests
tests.add('1 1\n', '0\n')

tests.add('2 2\n', '0\n')
tests.add('2 1\n', '1\n')

tests.add('3 3\n', '0\n')
tests.add('3 2\n', '3\n')
tests.add('3 1\n', '2\n')

tests.add('4 4\n', '4\n')

tests.add('5 5\n', '0\n')
tests.add('5 4\n', '20\n')

tests.add('6 6\n', '0\n')
tests.add('6 5\n', '60\n')

tests.add('7 7\n', '534\n')
tests.add('7 5\n', '269\n')
tests.add('7 3\n', '37\n')

tests.add('8 8\n', '0\n')
tests.add('8 6\n', '1402\n')
tests.add('8 2\n', '14\n')

tests.add('9 9\n', '0\n')
tests.add('9 8\n', '23082\n')
tests.add('9 3\n', '83\n')
