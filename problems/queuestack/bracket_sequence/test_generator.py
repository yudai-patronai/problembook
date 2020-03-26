from lib.testgen import TestSet

tests = TestSet()

tests.add(
    '()\n',
    'YES\n'
)
tests.add(
    '{}[]\n',
    'YES\n'
)
tests.add(
    '{[}\n',
    'NO\n',
)
tests.add(
    '()(((\n',
    'NO\n'
)
tests.add(
    '([()][][{}(){}][]({([]())})[]\n',
    'NO\n'
)
tests.add(
    '([()][][{}(){}][]{([]())})[]\n',
    'YES\n'
)
