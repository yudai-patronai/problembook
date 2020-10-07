from copy import copy
from random import randrange, choice

from lib.testgen import TestSet


tests = TestSet()

# statement tests, basic functionality
tests.add(
"""1 7
0 ? 1 0
0 + 1 2
0 ? 1 0
0 + 1 3
0 ? 1 0
0 - 1 0
0 ? 1 0
""", '0\n2\n3\n0\n'
)

tests.add(
"""2 7
0 + 1 5
1 + 1 6
0 ? 1 0
1 ? 1 0
1 - 1 0
1 ? 1 0
0 ? 1 0
""", '5\n6\n0\n5\n'
)

# indicator of slow input/output
tests.add('1 3000000\n0 + 0 1' + '\n'.join(['0 ? 0 0'] * 2999999), '1\n' * 2999999)

# stress tests
def generate_test_fill_and_clear(tables_num, queries_num, elements_max):
    tables = [dict() for _ in range(tables_num)]
    partition = queries_num // 5
    inp = []
    outp = []

    # fill
    for _ in range(partition):
        table, key, value = randrange(tables_num), randrange(elements_max), randrange(elements_max)
        inp.append(' '.join((str(table), '+', str(key), str(value))))
        tables[table][key] = value
        if randrange(2):
            key = randrange(elements_max)
            value = tables[table].get(key, 0)
        inp.append(' '.join((str(table, '?', str(key), '0'))))
        outp.append(value)
    
    # check
    table_keys = [list(table.keys()) for table in tables]
    for _ in range(partition):
        table = randrange(tables_num)
        if len(table_keys[table]) and randrange(2):
            key = choice(tables_keys[table])
        else:
            key = randrange(elements_max)
        inp.append(' '.join((str(table), '?', str(key), '0')))
        outp.append(tables[table].get(key, 0))

    # clear
    for _ in range(partition):
        table = randrange(tables_num)
        if len(table_keys[table]):
            key = choice(tables_keys[table])
        else:
            key = randrange(elements_max)
        inp.append(' '.join(str(table), '-', str(key), '0'))
        tables[table].pop(key, None)
        if randrange(2):
            key = ranrange(elements_max)
        value = tables[table].get(key, 0)
        inp.append(' '.join((str(table), '?', str(key), '0')))
        outp.append(value)

    test_input = str(tables_num) + ' ' + str(partition * 5) + '\n' + '\n'.join(inp)
    test_output = '\n'.join(map(str, outp))
    return test_input, test_output

def generate_test_random(tables_num, queries_num, elements_max):
    tables = [dict() for _ in range(tables_num)]
    ops = ['+', '+', '?', '?', '-']
    inp = []
    outp = []

    for _ in range(queries_num):
        table, key, value = randrange(tables_num), randrange(elements_max), randrange(elements_max)
        op = choice(ops)
        inp.append(' '.join((str(table), op, str(key), str(value))))
        if op == '+':
            tables[table][key] = value
        if op == '-':
            tables[table].pop(key, None)
        if op == '?':
            outp.append(tables[table].get(key, value))

    test_input = str(tables_num) + ' ' + str(queries_num) + '\n' + '\n'.join(inp)
    test_output = '\n'.join(map(str, outp))
    return test_input, test_output

# stress: num of queries much more than elements range, rewrites and double deletes
tests.add(*generate_test_fill_and_clear(1, 100000, 200))
tests.add(*generate_test_fill_and_clear(1, 100000, 200))
tests.add(*generate_test_random(1, 100000, 200))
tests.add(*generate_test_random(1, 100000, 200))

# stress: sparse table
tests.add(*generate_test_fill_and_clear(1, 100000, 10000000))
tests.add(*generate_test_fill_and_clear(1, 100000, 10000000))
tests.add(*generate_test_random(1, 100000, 10000000))
tests.add(*generate_test_random(1, 100000, 10000000))

# stress: repeat with lots of tables
tests.add(*generate_test_fill_and_clear(100, 100000, 200))
tests.add(*generate_test_random(100, 100000, 200))

tests.add(*generate_test_fill_and_clear(100, 100000, 10000000))
tests.add(*generate_test_random(100, 100000, 10000000))

# asymptotic test: aggressive write
def aggressive_write():
    for n in range(2999999):
        inp.append('0 + ' + str(n) + ' 0')
    test_input = '\n'.join(('1 3000000', '\n'.join(inp), '0 ? 0 1'))
    test_output = '0\n'
    return test_input, test_output
tests.add(*aggressive_write)
