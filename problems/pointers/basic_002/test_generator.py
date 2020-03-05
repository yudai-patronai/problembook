# test_generator.py
from lib.testgen import TestSet

tests = TestSet()
tests.add('1 2\n', '2 1\n')
tests.add('3 4\n', '4 3\n')  
tests.add('4 1\n', '1 4\n')
tests.add('6 7\n', '7 6\n')
tests.add('8 3\n', '3 8\n')

