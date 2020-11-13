def swap_rows(M, p, q):
    if p == q:
        return None
    for j in range(len(M)):
        M[p][j], M[q][j] = M[q][j], M[p][j]


def find_max_diag(M):
    N = len(M)
    max_elem, max_elem_i = M[0][0], 0
    for i in range(N):
        for j in range(N):
            if i == j:
                if M[i][j] > max_elem:
                    max_elem = M[i][j]
                    max_elem_i = i
    return max_elem_i


N, K = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

swap_diag = find_max_diag(matrix)
swap_rows(matrix, swap_diag, K)

for row in matrix:
    print(*row)
