from lib.testgen import TestSet

tests = TestSet()

mayas_dec = [
    ('..|', 7),
    ('.| @', 120),
    ('. @ @', 400),
    ('@', 0),
    ('....|||', 19),
    ('.| @ ..||', 6 * 20**2 + 0 + 12),
    ('..|| .|| @ @', 12*20**3 + 11*20**2 + 0 + 0),
    ('. @ .| @ @ ..||', 20**5 + 0 + 6*20**3 + 0 + 0 + 12),
]

for maya, dec in mayas_dec:
    quest = maya + '\n'
    ans = str(dec) + '\n'

    tests.add(quest, ans)