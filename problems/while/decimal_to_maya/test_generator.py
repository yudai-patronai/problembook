from lib.testgen import TestSet

tests = TestSet()

dec_maya = [
    (7, '..|'),
    (120, '.| @'),
    (400, '. @ @'),
    (0, '@'),
    (19, '....|||'),
    (6 * 20**2 + 0 + 12, '.| @ ..||'),
    (12*20**3 + 11*20**2 + 0 + 0, '..|| .|| @ @'),
    (20**5 + 0 + 6*20**3 + 0 + 0 + 12, '. @ .| @ @ ..||'),
]

for dec, maya in dec_maya:
    tests.add(
        str(dec) + '\n',
        maya + '\n'
    )
