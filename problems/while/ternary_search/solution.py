def ternary_search(f, left, right):
    while abs(right - left) > 1e-5:
        m1 = (2*left + right) / 3
        m2 = (left + 2*right) / 3
        if f(m1) < f(m2):
            left = m1
        else:
            right = m2
    return (left+right)/2, f((left+right)/2)
    