def split_barrier(A, barrier):
    L, M, R = [], [], []
    for elem in A:
        if elem < barrier:
            L.append(elem)
        elif elem == barrier:
            M.append(elem)
        else:
            R.append(elem)
    j = 0
    for elem in L + M + R:
        A[j] = elem
        j += 1
