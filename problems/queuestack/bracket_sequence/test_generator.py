from lib.testgen import TestSet

tests = TestSet()

tests.add(
    '()',
    'YES'
)
tests.add(
    '{[}',
    'NO',
)
tests.add(
    '(]',
    'NO'
)
tests.add(
    ')(',
    'NO'
)
tests.add(
    '{}[]',
    'YES'
)
tests.add(
    '{(){}]',
    'NO'
)
tests.add(
    '()(((',
    'NO'
)
tests.add(
    '([()][][{}(){}][]({([]())})[]',
    'NO'
)
tests.add(
    '([()][][{}(){}][]{([]())})[]',
    'YES'
)
