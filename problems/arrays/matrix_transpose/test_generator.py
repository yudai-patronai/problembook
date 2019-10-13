from lib.testgen import TestSet

tests = TestSet()

def arr2d_to_str(arr):
    s = ""
    for row in arr:
        s += " ".join(row) + '\n'
    return s

def question(arr):
    s = str(len(arr)) + '\n'
    s += arr2d_to_str(arr)
    return s

tests.add(
    question(
        [['a', 'b'],
         ['c', 'd']]
    ),
    arr2d_to_str(
        [['a', 'c'],
         ['b', 'd']]
    )
)
tests.add(
    question(
        [['1', '0'],
         ['0', '1']]
    ),
    arr2d_to_str(
        [['1', '0'],
         ['0', '1']]
    )
)
tests.add(
    question(
        [['1', '2', '3'],
         ['a', 'b', 'c'],
         ['4', '5', '6']]
    ),
    arr2d_to_str(
        [['1', 'a', '4'],
         ['2', 'b', '5'],
         ['3', 'c', '6']]
    )
)
tests.add(
    question(
        [['1', '2', '3', '4'],
         ['5', '6', '7', '8'],
         ['a', 'b', 'c', 'd'],
         ['e', 'f', 'g', 'h']]
    ),
    arr2d_to_str(
        [['1', '5', 'a', 'e'],
         ['2', '6', 'b', 'f'],
         ['3', '7', 'c', 'g'],
         ['4', '8', 'd', 'h']]
    )
)
tests.add(
    question(
        [['abc', 'cde'],
         ['fgh', 'abc']]
    ),
    arr2d_to_str(
        [['abc', 'fgh'],
         ['cde', 'abc']]
    )
)