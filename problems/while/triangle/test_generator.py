from lib.testgen import TestSet


def get_triangle(N):
    counter = 1
    triangle = ''
    for i in range(1, N+1):
        row = ''
        for j in range(i):
            if j != i-1:
                row += str(counter) + ' '
            else:
                row += str(counter)
            counter += 1
        triangle += row + '\n'
    return triangle


tests = TestSet()

for i in range(1, 10):
    triangle = get_triangle(i)
    tests.add(
        str(i) + '\n',
        triangle
    )

tests.add(
    str(23) + '\n',
    get_triangle(23)
)
