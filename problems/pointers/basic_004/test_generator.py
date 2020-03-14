# test_generator.py
from lib.testgen import TestSet

tests = TestSet()
tests.add('1\n 5\n', '5\n')
tests.add('0\n', '0\n')  
tests.add('5\n1 2 3 4 5\n', '15\n')
tests.add('6\n6 6 6 6 6 6\n', '36\n')
tests.add('10\n4 -5 387 -5 -1 58 -85 385 -587 85\n', '236\n')

