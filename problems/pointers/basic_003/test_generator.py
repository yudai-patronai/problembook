# test_generator.py
from lib.testgen import TestSet

tests = TestSet()
tests.add('5 6\n', '5\n')
tests.add('-1 -3\n', '-3\n')  
tests.add('-1 5\n', '-1\n')
tests.add('-100 500\n', '-50000\n')
tests.add('90 -60\n', '90\n')
tests.add('-5 -3\n', '-3\n')
tests.add('-6 5\n', '-1\n')
tests.add('-6 4\n', '-2\n')
