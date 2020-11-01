def det(matrix):
    res = 0
    if len(matrix) == 1:
        res = matrix[0][0]
    else:
        for i in range(len(matrix)):
            res += (-1) ** i * matrix[0][i] * det([minor[:i] + minor[i+1:] for
                                                   minor in matrix[1:]])

    return res


if __name__ == '__main__':
    n = int(input())
    matrix = []

    for _ in range(n):
        matrix.append([int(x) for x in input().split()])

    print(str(det(matrix)))
