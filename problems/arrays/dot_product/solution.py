def dot_product(N, v1, v2):
    s = 0
    for i in range(N):
        s += v1[i] * v2[i]
    return(s)