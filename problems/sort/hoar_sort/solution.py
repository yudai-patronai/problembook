def hoar_sort(A, depth=1, part='left'):
    print('depth:', depth, 'part:', part, 'array before:', A)
    if len(A) <= 1:
        return

    barrier = A[0]

    L, M, R = [], [], []
    for elem in A:
        if elem < barrier:
            L.append(elem)
        elif elem == barrier:
            M.append(elem)
        else:
            R.append(elem)

    hoar_sort(L, depth + 1, 'left')
    hoar_sort(R, depth + 1, 'right')

    j = 0
    for elem in L + M + R:
        A[j] = elem
        j += 1
    print('depth:', depth, 'part:', part, 'array after:', A)
