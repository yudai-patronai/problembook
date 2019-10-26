#!/usr/bin/env python3

from lib.testgen import TestSet

tests = TestSet()
tests.add('0\n', '1 0\n')
tests.add('1\n', '1 0\n')
tests.add('6\n', '4 4\n')
tests.add('10\n', '6 6\n')
tests.add('14\n', '9 9\n')
tests.add('20\n', '13 12\n')
tests.add('25\n', '16 16\n')
tests.add('30\n', '19 19\n')
tests.add('77\n', '48 48\n')
tests.add('37\n', '23 23\n')

