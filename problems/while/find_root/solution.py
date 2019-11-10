def find_root(f, a, b, tol):
    while (b - a) > tol:
        x = (b + a) / 2.
        val = f(x)
        if abs(val) < eps:
            return x
        elif f(a) * val > 0.:
            a = x
        else:
            b = x
    return x
