def transpose(A):
    N = len(A)
    for i in range(N):
        for j in range(i):
            A[i][j], A[j][i] = A[j][i], A[i][j]
