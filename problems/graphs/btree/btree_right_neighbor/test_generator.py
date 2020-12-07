# test_generator.py
from lib.testgen import TestSet

tests = TestSet()
tests.add('8\n10 7 15 3 8 13 18 9\n2', '3 8 13 18\n')
tests.add('6\n30 15 45 20 49 25\n2', '20 49\n')  
tests.add('10\n50 25 75 90 80 95 76 85 93 100\n4', '76 85 93 100\n')
tests.add('10\n0 1 2 3 4 5 6 7 8 9\n7', '7\n')
tests.add('0 0\n', '\n')

