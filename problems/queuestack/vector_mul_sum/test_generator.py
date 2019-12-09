from lib.testgen import TestSet

tests = TestSet()

tests.add(
    '1,2,3 4,5,6 +\n',
    '5,7,9\n'
)
tests.add(
    '1,2,3 4,5,6 *\n',
    '-3,-6,-3\n'
)
tests.add(
    '1,2,3 4,5,6 * 1,2,3 4,5,6 * +\n',
    '-6,-12,-6\n',
)
tests.add(
    '-1,-2,-3 2,4,6 + 4,5,6 *\n',
    '-3,-6,-3\n'
)
tests.add(
    '1,2,3 4,5,6 * 1,2,3 *\n',
    '-12,-6,0\n'
)
tests.add(
    '1,2,3 4,5,6 * 1,2,3 * 12,6,0 +\n',
    '0,0,0\n'
)