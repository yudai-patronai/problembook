from lib.testgen import TestSet

tests = TestSet()

tests.add(
    'In reverse Polish notation, the operators follow their operands;\n',
    '54\n'
)
tests.add(
    'Another example:\n',
    '14\n',
)
tests.add(
    'Keep calm!? It is not possible.\n',
    '23\n'
)
tests.add(
    'a .,!?:;\n',
    '1\n'
)
