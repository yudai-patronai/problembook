from lib.testgen import TestSet
from lib.random import sample

tests = TestSet()
tests.add('6\n1 2 3 4 5 6\n', 'NO\n')
tests.add('1\n34612\n', 'YES\n')
tests.add('5\n5 3 6 3 1\n', 'YES\n')
tests.add('2\n1 1\n', 'YES\n')
tests.add('1\n5\n', 'NO\n')