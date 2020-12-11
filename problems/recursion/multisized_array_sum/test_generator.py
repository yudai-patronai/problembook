from lib.testgen import TestSet
from test_collection import __manual_tests


# q: test_index
# a: sum

tests = TestSet()
for i, t in enumerate(__manual_tests):
    s, ds = t
    tests.add(str(i) + '\n', str(s) + '\n')
