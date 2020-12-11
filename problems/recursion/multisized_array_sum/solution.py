def multidim_sum(A):
    if len(A) == 0:
        return 0
    else:
        s = 0
        for a in A:
            if isinstance(a, list):
                s += multidim_sum(a)
            else:
                s += a
    return s
