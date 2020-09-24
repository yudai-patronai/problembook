from lib.testgen import TestSet

tests = TestSet()
tests.add('0 10 5 15\n', '[5,10]6\n')
tests.add('0 10 11 25\n', '[]0\n')
tests.add('0 10 10 15\n', '[10,10]1\n')
tests.add('-10 10 -5 5\n', '[-5,5]11\n')
tests.add('-5 5 -10 10\n', '[-5,5]11\n')
tests.add('-10 10 -5 5 1 0\n', '[]0\n')
tests.add('0 1 0 10 -10 1 -1 20 -65000 65000\n','[0,1]2\n')
tests.add('-65000 65000 -1 20 -10 1 0 10 0 1\n', '[0,1]2\n')