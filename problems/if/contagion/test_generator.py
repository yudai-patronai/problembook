#!/usr/bin/python3

from lib.testgen import TestSet

tests = TestSet()

tests.add('0 36.6 0 1 0 0 0 1 1 0\n', '3\n')

#          a   b  c d e f g h i j     group
tests.add('1 37.0 1 1 0 0 0 0 1 1\n', '1\n')
tests.add('0 37.5 1 0 0 0 0 0 0 1\n', '2\n')
tests.add('0 39.0 0 0 0 1 0 0 0 0\n', '2\n')
tests.add('0 37.6 0 0 1 0 1 0 1 0\n', '2\n')
tests.add('0 38.0 0 0 0 0 1 0 0 0\n', '2\n')
tests.add('0 38.0 0 0 0 0 0 0 1 0\n', '3\n')
tests.add('1 37.4 0 1 0 0 0 1 0 0\n', '3\n')

#          a   b  c d e f g h i j     group
tests.add('0 36.6 1 1 0 0 0 0 1 0\n', '2\n')
tests.add('0 36.6 1 1 0 1 0 1 0 1\n', '2\n')
tests.add('0 36.6 1 0 1 0 0 0 0 0\n', '3\n')
tests.add('0 36.6 1 0 0 1 0 0 0 0\n', '3\n')
tests.add('0 37.4 1 1 0 0 0 1 0 0\n', '4\n')
tests.add('0 36.6 0 0 0 0 1 0 0 0\n', '3\n')
tests.add('0 36.6 0 0 0 0 0 0 0 1\n', '4\n')

