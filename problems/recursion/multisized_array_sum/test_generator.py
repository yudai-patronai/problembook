from lib.testgen import TestSet
from header import __manual_tests


# qusettion: test_index of __manual_tests
# answer: correct sum

tests = TestSet()
for i, t in enumerate(__manual_tests):
    s, ds = t
    tests.add(str(i) + '\n', str(s) + '\n')
