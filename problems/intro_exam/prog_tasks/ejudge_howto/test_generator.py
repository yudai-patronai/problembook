from lib.testgen import TestSet

def ans(s):
    return 'Hello, {}!\n'.format(ans)

tests = TestSet()

for x in ['FEFM', 'Ejudge', 'phystech', 'CS', 'kdkjadjka adlkawd;']:
    tests.add(x, ans(x))
