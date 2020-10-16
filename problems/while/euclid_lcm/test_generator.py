from lib.testgen import TestSet


manual = [
    (4, 5, 20),
    (81, 9, 81),
    (18, 24, 72),
    (0, 100, 0),  # zero arg
    (91_239, 8648,  789_034_872),
    (121_931, 9123, 1_112_376_513),  #
    (9123, 121_931, 1_112_376_513),  # arg swap
]

tests = TestSet()
for a, b, lcm in manual:
    tests.add(
        '{}\n{}\n'.format(a, b),
        '{}\n'.format(lcm)
    )
