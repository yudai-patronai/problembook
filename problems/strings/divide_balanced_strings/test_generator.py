from lib.testgen import TestSet

tests = TestSet()

# from statement
tests.add('(()())', '1\n')
tests.add('()(())()()', '4\n')

# trivial
tests.add('()', '1')

# asymptotic tests
test.add('()' * 50000, '50000')
test.add('(' * 50000 + ')' * 50000, '1')
