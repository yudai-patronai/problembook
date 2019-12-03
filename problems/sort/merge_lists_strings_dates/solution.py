def weight(M):
    # вычисляет вес даты - кол-во секунд
    weigths = {'m': 60, 's': 1, 'h': 3600}
    keys = tuple(weigths.keys())

    secs = 0
    quantifier = ''
    for char in M:
        if char in keys:
            secs += int(quantifier) * weigths[char]
            quantifier = ''
        else:
            quantifier += char

    return secs


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
