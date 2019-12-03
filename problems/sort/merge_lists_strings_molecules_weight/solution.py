def weight(M):
    # вычисляет вес молекулы
    weigths = {'C': 12, 'H': 1, 'N': 14, 'O': 16}
    atoms = tuple(weigths.keys())

    current_atom = M[0]
    molweight = 0
    count = ''
    for char in M[1:]:
        if char in atoms:
            count = 1 if not count else int(count)
            molweight += weigths[current_atom] * count

            current_atom = char
            count = ''
        else:
            count += char

    count = 1 if not count else int(count)
    molweight += weigths[current_atom] * count

    return molweight


def merge_by_weight(L, R):
    len_L, len_R = len(L), len(R)
    
    A = [0] * (len_L + len_R)
    ind_L = ind_R = ind_A = 0
    
    while ind_L < len_L and ind_R < len_R:
        if weight(L[ind_L]) <= weight(R[ind_R]):
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

L = input().split()
R = input().split()

A = merge_by_weight(L, R)

print(" ".join(A))
