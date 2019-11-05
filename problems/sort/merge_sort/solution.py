def merge(L, R):
    len_L, len_R = len(L), len(R)

    A = [0] * (len_L + len_R)
    ind_L = ind_R = ind_A = 0

    while ind_L < len_L and ind_R < len_R:
        if L[ind_L] <= R[ind_R]:
            A[ind_A] = L[ind_L]
            ind_L += 1
            ind_A += 1
        else:
            A[ind_A] = R[ind_R]
            ind_R += 1
            ind_A += 1

    while ind_L < len_L:
        A[ind_A] = L[ind_L]
        ind_A += 1
        ind_L += 1

    while ind_R < len_R:
        A[ind_A] = R[ind_R]
        ind_A += 1
        ind_R += 1

    return A


def merge_sort(A, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', A)

    if len(A) <= 1:
        return

    middle = len(A) // 2
    L = A[:middle]
    R = A[middle:]
    merge_sort(L, depth + 1, 'left')
    merge_sort(R, depth + 1, 'right')
    C = merge(L, R)

    for i in range(len(A)):
        A[i] = C[i]

    print('depth:', depth, '|', 'part:', part, '|', 'after merge:', A)