# test_generator.py
from lib.testgen import TestSet

tests = TestSet()
# Some basic tests
tests.add('3\n17 180 90 37.6\n62 170 70 38.2\n40 160 60 36.9\n', '38.2')
tests.add('3\n17 180 60 37.1\n29 174 85 39.1\n40 160 50 36.9\n', '38.1')
tests.add('3\n10 130 30 37.6\n65 170 70 38.4\n40 160 52 38.2\n', '38.3')
tests.add('5\n32 170 250 37.3\n20 150 200 37.5\n34 170 70 38.9\n57 155 60 37.5\n45 160 65 36.5\n', '37.4')
tests.add('2\n32 170 70 37.3\n20 160 65 37.5\n', '0')

