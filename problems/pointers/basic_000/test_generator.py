# test_generator.py
from lib.testgen import TestSet

tests = TestSet()
tests.add('1 2 3 4 5 6\n', '1 2 3 4 5 6\n')
tests.add('-9 -8 -7 -6 -5 -4\n', '-9 -8 -7 -6 -5 -4\n')  
