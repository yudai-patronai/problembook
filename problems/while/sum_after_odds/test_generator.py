from lib.testgen import TestSet

tests = TestSet()

def join_ints(arr):
    return "\n".join(map(str, arr)) + '\n'

tests.add(
    join_ints([1, 2, 3, 4, 5, 0]),
    str(6)
)
tests.add(
    join_ints([1, 2, 2, 4, 7, 2, 5, 0]),
    str(4)
)
tests.add(
    join_ints([1, 8, 7, 3, 0]),
    str(11)
)
tests.add(
    join_ints([1, 1, 1, 1, 1, 1, 0]),
    str(5)
)
tests.add(
    join_ints([2, 2, 2, 2, 2, 0]),
    str(-1)
)
tests.add(
    join_ints([2, 2, 2, 2, 2, 1, 1, 1, 0]),
    str(2)
)
tests.add(
    join_ints([0]),
    str(-1)
)
tests.add(
    join_ints([2, 0]),
    str(-1)
)

# tests.add(
#     join_ints([]),
#     str()
# )
