__manual_tests = [
    (
        0,  # sum
        []  # datastracture
    ),
    (
        6,
        [1, 2, 3]
    ),
    (
        15,
        [1, [1, 2, [1, 2, 3], []], [[1, 2], 2]]
    ),
    (
        16,
        [1, [1, 2, [1, [1, [0, [], 1]], [[-1, 3, 1, [0, 1, -2]], 2]], []], [[1, 2], 2]]
    ),
    (
        28,
        [0, [1, [2, [3, [4, [5, [6, [7]]]]]]]]
    ),
    (
        10,
        [[[[[0], 1], 2], 3], 4],
    ),
    (
        50,
        [0, [1, [3, [7, [8, 10], 9], 6], 4], 2]
    )
]
